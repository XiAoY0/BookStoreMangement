-- 修改购买记录表，添加外键约束
ALTER TABLE 购买记录
ADD CONSTRAINT fk_member_id FOREIGN KEY (会员编号) REFERENCES 会员(会员编号),
ADD CONSTRAINT fk_book_id FOREIGN KEY (图书编号) REFERENCES 图书(图书编号);

-- 修改退书记录表，添加外键约束
ALTER TABLE 退书记录
ADD CONSTRAINT fk_return_member_id FOREIGN KEY (会员编号) REFERENCES 会员(会员编号),
ADD CONSTRAINT fk_return_book_id FOREIGN KEY (图书编号) REFERENCES 图书(图书编号);

