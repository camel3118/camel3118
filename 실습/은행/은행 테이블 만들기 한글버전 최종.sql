create table 고객정보(
계좌번호 varchar(50) not null primary key,
계좌형태 varchar(50) not null,
예금주 varchar(50) not null,
생년월일 date not null,
비밀번호 int not null,
잔액 int not null default 0,
개설일 datetime not null default now(),
만기해지일 varchar(50));


create table 입출금통장(
거래일 datetime not null default now(),
계좌번호 varchar(50) not null,
예금주 varchar(50) not null,
입금액 int not null default 0,
출금액 int not null default 0,
보낸분_받는분 varchar(50),
잔액 int not null default 0,
constraint 입출금통장_fk_account
foreign key (계좌번호) references 고객정보(계좌번호) on delete cascade);


create table 적금통장(
거래일 datetime not null default now(),
계좌번호 varchar(50) not null,
예금주 varchar(50),
입금액 int not null default 0,
잔액 int not null default 0,
만기일 varchar(50),
constraint 적금통장_fk_account
foreign key (계좌번호) references 고객정보(계좌번호) on delete cascade);




