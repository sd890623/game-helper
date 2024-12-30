
import express from 'express'
import bodyParser from 'body-parser'
import crypto from 'crypto'

const app = express();
app.use(bodyParser.json());

// 模拟数据库存储
const db = {
    // 存储已激活的 CDKey
    activations: new Map(),
    // 模拟CDKey数据库
    cdkeys: new Map([
        ['TEST-KEY-123', {
            maxActivations: 1,
            features: ['feature1', 'feature2', 'feature3'],
            expiryDate: '2024-12-31',
            isValid: true
        }],
        ['PRO-KEY-456', {
            maxActivations: 3,
            features: ['feature1', 'feature2', 'feature3', 'feature4'],
            expiryDate: '2024-12-31',
            isValid: true
        }]
    ])
};

// 验证CDKey的中间件
const validateCDKey = (req, res, next) => {
    const { cdkey, machine_id } = req.body;

    if (!cdkey || !machine_id) {
        return res.status(400).json({
            verified: false,
            message: '无效的请求参数'
        });
    }

    // 检查CDKey格式
    const cdkeyPattern = /^[A-Z]+-[A-Z]+-\d{3}$/;
    if (!cdkeyPattern.test(cdkey)) {
        return res.status(400).json({
            verified: false,
            message: '无效的CDKey格式'
        });
    }

    // 检查machine_id格式（应该是64字符的十六进制）
    const machineIdPattern = /^[a-f0-9]{64}$/i;
    if (!machineIdPattern.test(machine_id)) {
        return res.status(400).json({
            verified: false,
            message: '无效的机器ID'
        });
    }

    next();
};

// 验证接口
app.post('/api/verify', validateCDKey, (req, res) => {
    const { cdkey, machine_id } = req.body;
    
    // 检查CDKey是否存在
    const keyData = db.cdkeys.get(cdkey);
    if (!keyData) {
        return res.json({
            verified: false,
            message: 'CDKey不存在'
        });
    }

    // 检查CDKey是否有效
    if (!keyData.isValid) {
        return res.json({
            verified: false,
            message: 'CDKey已被禁用'
        });
    }

    // 检查是否过期
    const expiryDate = new Date(keyData.expiryDate);
    if (expiryDate < new Date()) {
        return res.json({
            verified: false,
            message: 'CDKey已过期'
        });
    }

    // 获取当前CDKey的激活记录
    let activationRecord = db.activations.get(cdkey) || [];

    // 检查是否已经在此机器上激活
    const existingActivation = activationRecord.find(
        record => record.machine_id === machine_id
    );
    
    if (existingActivation) {
        // 如果已经在此机器上激活，直接返回成功
        return res.json({
            verified: true,
            message: '验证成功',
            features: keyData.features,
            verification_token: existingActivation.token
        });
    }

    // 检查激活次数是否超限
    if (activationRecord.length >= keyData.maxActivations) {
        return res.json({
            verified: false,
            message: `已达到最大激活次数 (${keyData.maxActivations})`
        });
    }

    // 生成验证token
    const token = crypto.randomBytes(32).toString('hex');

    // 记录新的激活
    activationRecord.push({
        machine_id,
        activationDate: new Date().toISOString(),
        token
    });

    // 更新数据库
    db.activations.set(cdkey, activationRecord);

    // 返回成功响应
    res.json({
        verified: true,
        message: '验证成功',
        features: keyData.features,
        verification_token: token,
        expiry_date: keyData.expiryDate
    });
});

// 状态检查接口
app.post('/api/check-status', validateCDKey, (req, res) => {
    const { cdkey, machine_id } = req.body;
    
    const keyData = db.cdkeys.get(cdkey);
    const activationRecord = db.activations.get(cdkey) || [];
    
    const isActivated = activationRecord.some(
        record => record.machine_id === machine_id
    );

    res.json({
        verified: isActivated && keyData?.isValid && new Date(keyData.expiryDate) > new Date(),
        active: isActivated
    });
});

// 启动服务器
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`服务器运行在端口 ${PORT}`);
});

// 测试用的其他辅助接口

// 获取所有激活记录（仅供测试）
app.get('/api/activations', (req, res) => {
    const activations = {};
    db.activations.forEach((value, key) => {
        activations[key] = value;
    });
    res.json(activations);
});

// 手动添加CDKey（仅供测试）
app.post('/api/add-cdkey', (req, res) => {
    const { cdkey, maxActivations, features, expiryDate } = req.body;
    
    if (!cdkey || !maxActivations || !features || !expiryDate) {
        return res.status(400).json({ message: '缺少必要参数' });
    }

    db.cdkeys.set(cdkey, {
        maxActivations,
        features,
        expiryDate,
        isValid: true
    });

    res.json({ message: 'CDKey添加成功' });
});