USE mydb;
CREATE TABLE `emp4` (
	`empno` SMALLINT NOT NULL AUTO_INCREMENT,
    `ename` VARCHAR(16) NOT NULL,
    `job` VARCHAR(16) DEFAULT NULL,
    #PRIMARY KEY(`empno`)
    INDEX `empno_index` (`empno`) #empno可重複新增
    )AUTO_INCREMENT=32760 ENGINE=InnoDB DEFAULT CHARSET =big5
#SMALLINT -32768~32767 0~65535
# -128~127  0~127,-1~-128  0~255