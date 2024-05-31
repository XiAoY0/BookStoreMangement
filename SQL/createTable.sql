use bookmanage;
-- 会员表
CREATE TABLE 会员 (
    会员编号 INT PRIMARY KEY,
    会员姓名 VARCHAR(50),
    会员性别 VARCHAR(10),
    会员类别 VARCHAR(50),
    会员联系方式 VARCHAR(50)
);

-- 工作人员表
CREATE TABLE 工作人员 (
    员工编号 INT PRIMARY KEY,
    员工姓名 VARCHAR(50),
    员工性别 VARCHAR(10),
    员工身份证号 VARCHAR(20),
    员工职位 VARCHAR(50),
    员工工资 DECIMAL(10, 2)
    员工密码 VARCHAR(50)
);

-- 图书表
CREATE TABLE 图书 (
    图书编号 INT PRIMARY KEY,
    图书名称 VARCHAR(100),
    图书出版社 VARCHAR(100),
    图书价格 DECIMAL(10, 2),
    图书作者 VARCHAR(100),
    图书类别 VARCHAR(50),
    图书库存数量 INT
);

-- 购买记录表
CREATE TABLE 购买记录 (
    购买记录编号 INT PRIMARY KEY,
    购买时间 DATETIME,
    会员编号 INT,
    会员联系方式 VARCHAR(50),
    会员姓名 VARCHAR(50),
    会员类别 VARCHAR(50),
    图书编号 INT,
    图书名称 VARCHAR(100),
    办理人 VARCHAR(50),
    FOREIGN KEY (会员编号) REFERENCES 会员(会员编号),
    FOREIGN KEY (图书编号) REFERENCES 图书(图书编号)
);

-- 退书记录表
CREATE TABLE 退书记录 (
    退款记录编号 INT PRIMARY KEY,
    退款时间 DATETIME,
    会员编号 INT,
    会员联系方式 VARCHAR(50),
    会员姓名 VARCHAR(50),
    图书编号 INT,
    图书名称 VARCHAR(100),
    办理人 VARCHAR(50),
    FOREIGN KEY (会员编号) REFERENCES 会员(会员编号),
    FOREIGN KEY (图书编号) REFERENCES 图书(图书编号)
);
