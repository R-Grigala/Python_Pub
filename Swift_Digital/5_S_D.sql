if exists
	(select name from sys.databases
	where name='School'
	)

Drop database School

GO

Create database School

Use School

if OBJECT_ID ('Teacher', 'U')
is not null
create table Teacher
(
Teacher_ID char(11) primary key,
Teacher_name nvarchar(20) not null,
Teacher_sname nvarchar(20) not null,
Teacher_gender nvarchar(20), 
Teacher_subject nvarchar(20)
)

if OBJECT_ID ('Pupil', 'U')
is not null
create table Pupil
(
Pupil_ID char(11) primary key,
Pupil_name nvarchar(20),
Pupil_sname nvarchar(20),
Pupil_gender nvarchar(20),
Pupil_class int 
)

-----------------------------

if OBJECT_ID ('Teacher_Pupil', 'U')
is not null
drop table Teacher_Pupil
go
create table Teacher_Pupil
(
Teacher_ID char(11) unique constraint fk_Teacher_Pupil  references Teacher(Teacher_ID)
		on update cascade,
Pupil_ID char(11) constraint fk_Pupil_Teacher  references Pupil(Pupil_ID)
		on update cascade
)

insert into Teacher
values
('560010',N'ნინო',N'ტაბატაძე',N'მდედრობითი',N'English'),
('570010',N'გოჩა',N'არველაძე',N'მამრობითი',N'Mathematics')

--select * from Teacher


insert into Pupil
values
('660010',N'გიორგი',N'ლომიძე',N'მამრობითი',6),
('670010',N'მაია',N'არჩვაძე',N'მდედრობითი',7)

--select * from Pupil


insert into Teacher_Pupil
values
('560010','660010'),
('570010','660010'),
('560010','670010')

