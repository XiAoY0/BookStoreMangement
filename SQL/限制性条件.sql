ALTER TABLE 工作人员
  MODIFY 员工性别 ENUM('男', '女') NOT NULL;

ALTER TABLE 会员
  MODIFY 会员性别 ENUM('男', '女') NOT NULL;

ALTER TABLE 会员
  MODIFY 会员联系方式 VARCHAR(11) NOT NULL,
  ADD CONSTRAINT chk_contact_length_new CHECK (CHAR_LENGTH(会员联系方式) = 10);

ALTER TABLE 会员
  MODIFY 会员类别 ENUM('普通会员', '高级会员', '白金会员', '黄金会员') NOT NULL;

ALTER TABLE 会员
  ADD COLUMN 折扣 VARCHAR(10) NOT NULL DEFAULT '5%' AFTER 会员类别;

-- 根据会员类别设置不同的默认折扣
-- 这需要在应用逻辑中处理，或者使用触发器

ALTER TABLE 图书
  MODIFY 图书名称 VARCHAR(100) NOT NULL,
  ADD CONSTRAINT chk_book_name CHECK (图书名称 LIKE '《%》');

ALTER TABLE 图书
  MODIFY 图书出版社 VARCHAR(100) NOT NULL,
  ADD CONSTRAINT chk_publisher CHECK (图书出版社 LIKE '%出版社' OR 图书出版社 LIKE '%书店' OR 图书出版社 LIKE '%馆' OR 图书出版社 LIKE '%出版公司');
	
ALTER TABLE 工作人员
  MODIFY 员工身份证号 VARCHAR(20) NOT NULL,
  ADD CONSTRAINT chk_identity_length CHECK (CHARACTER_LENGTH(员工身份证号) = 18);