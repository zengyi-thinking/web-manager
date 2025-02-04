# 学生信息管理系统

## 项目简介

本系统是一个现代化的教育管理平台，采用前后端分离架构，实现了学生、教师、课程三大模块的完整管理功能。系统界面简洁直观，功能完善，性能稳定，适用于教育机构的日常信息管理需求。

主要特点：

- 前后端分离架构
  - RESTful API 设计规范
  - 接口统一规范化处理
  - 前后端数据交互标准化
  - 错误处理机制完善
- 响应式设计
  - 支持 PC/平板/手机等多种设备
  - 界面布局自适应调整
  - 触控支持优化
  - 不同分辨率适配
- 数据验证机制
  - 前端实时数据校验
  - 后端二次验证保证
  - 数据完整性检查
  - 特殊字符过滤
- 查询功能
  - 多条件组合查询
  - 模糊搜索支持
  - 结果分页展示
  - 导出数据功能
- 模块化设计
  - 高内聚低耦合
  - 组件复用性强
  - 便于功能扩展
  - 维护成本低

## 系统预览

### 学生管理界面

<div align="center">
    <img src="docs/images/students/student-management.png" alt="学生管理界面" width="800"/>
    <p>学生信息管理界面 - 支持信息的增删改查和多条件搜索</p>
</div>

主要功能：

- 学生基本信息管理
- 学籍信息维护
- 成绩管理
- 选课管理
- 数据导入导出

### 教师管理界面

<div align="center">
    <img src="docs/images/teachers/teacher-management.png" alt="教师管理界面" width="800"/>
    <p>教师信息管理界面 - 包含教师基本信息和课程关联管理</p>
</div>

主要功能：

- 教师基本信息管理
- 教师资质管理
- 授课信息管理
- 工资信息管理
- 考勤管理

### 课程管理界面

<div align="center">
    <img src="docs/images/courses/course-management.png" alt="课程管理界面" width="800"/>
    <p>课程信息管理界面 - 提供完整的课程信息管理功能</p>
</div>

主要功能：

- 课程基本信息管理
- 教学大纲管理
- 选课人数统计
- 成绩登记管理
- 学分学时管理

## 技术栈

### 前端技术

- Vue.js 2.x
  - Vue Router 路由管理
    - 路由懒加载
    - 路由权限控制
    - 页面切换动画
  - Vuex 状态管理
    - 集中式存储
    - 状态变更追踪
    - 模块化管理
  - 组件化开发
    - 可复用组件库
    - 生命周期管理
    - 父子组件通信
- Element UI
  - Form 表单组件
    - 数据校验
    - 自定义校验规则
    - 动态表单项
  - Table 表格组件
    - 自定义列模板
    - 排序/筛选
    - 固定表头/列
  - Dialog 对话框
    - 自定义内容
    - 异步关闭
    - 动画效果
- Axios
  - 请求/响应拦截
    - 统一错误处理
    - 请求参数处理
    - 响应数据处理
  - 取消请求
    - 防止重复提交
    - 超时处理
  - 并发请求
    - 多个请求并行
    - 请求队列管理

### 后端技术

- Python 3.x
  - 异步编程
    - 协程支持
    - 异步 IO
    - 并发处理
  - 类型注解
    - 代码可读性
    - IDE 智能提示
    - 错误预防
- Flask
  - 蓝图(Blueprint)
    - 模块化路由
    - 视图函数组织
    - URL 前缀设置
  - 中间件
    - 请求预处理
    - 响应后处理
    - 异常处理
  - 扩展支持
    - ORM 集成
    - 缓存支持
    - 邮件发送
- SQLAlchemy

  - 模型定义
    - 字段类型丰富
    - 关系映射
    - 约束条件
  - 查询构建
    - 链式调用
    - 复杂查询支持
    - 原生 SQL 支持
  - 会话管理
    - 事务支持
    - 并发控制
    - 缓存机制

- MySQL
  - 数据类型
    - 整型/浮点型
    - 字符串类型
    - 日期时间类型
  - 索引优化
    - 主键索引
    - 唯一索引
    - 复合索引
  - 事务特性
    - ACID 保证
    - 隔离级别
    - 死锁处理

## 核心功能

### 1. 学生管理模块

<div align="center">
    <img src="docs/images/students/student-crud.gif" alt="学生信息编辑" width="600"/>
</div>

#### 信息管理

- 基本信息
  - 学号(唯一标识)
  - 姓名
  - 性别
  - 年龄
  - 院系
  - 班级
  - 联系方式
- 学籍信息
  - 入学时间
  - 学籍状态
  - 专业方向
  - 培养层次
- 成绩信息
  - 课程成绩
  - 学分统计
  - 绩点计算
  - 排名信息

#### 数据操作

- 信息录入
  - 单条录入
  - 批量导入
  - 数据校验
  - 错误提示
- 信息修改
  - 单字段修改
  - 批量修改
  - 修改历史
  - 操作日志
- 信息删除
  - 单条删除
  - 批量删除
  - 删除确认
  - 数据备份

#### 查询功能

- 条件查询
  - 单条件查询
  - 多条件组合
  - 模糊匹配
  - 结果排序
- 高级查询
  - 区间查询
  - 关联查询
  - 统计查询
  - 自定义查询

### 2. 教师管理模块

<div align="center">
    <img src="docs/images/teachers/teacher-crud.gif" alt="教师信息编辑" width="600"/>
</div>

#### 基本信息

- 个人信息
  - 教师编号
  - 姓名
  - 性别
  - 出生日期
  - 学历学位
  - 专业领域
- 工作信息
  - 入职时间
  - 职称职务
  - 所属院系
  - 研究方向
  - 工作状态

#### 教学管理

- 授课信息
  - 授课课程
  - 课时统计
  - 教学评价
  - 教学成果
- 课程安排
  - 课程分配
  - 时间安排
  - 教室分配
  - 调课管理

#### 工资管理

- 基本工资
  - 岗位工资
  - 薪级工资
  - 绩效工资
  - 津贴补贴
- 课时费
  - 课时统计
  - 费率设置
  - 金额计算
  - 发放记录

### 3. 课程管理模块

<div align="center">
    <img src="docs/images/courses/course-crud.gif" alt="课程信息编辑" width="600"/>
</div>

#### 课程信息

- 基本信息
  - 课程编号
  - 课程名称
  - 课程类型
  - 开课院系
  - 学分学时
- 教学信息
  - 授课教师
  - 上课时间
  - 上课地点
  - 教材信息

#### 选课管理

- 选课设置
  - 选课时间
  - 人数限制
  - 先修课程
  - 冲突检测
- 选课统计
  - 选课人数
  - 退课统计
  - 课程评价
  - 成绩分布

#### 成绩管理

- 成绩录入
  - 平时成绩
  - 期末成绩
  - 总评成绩
  - 补考成绩
- 成绩统计
  - 及格率
  - 平均分
  - 分数段
  - 成绩排名

## 系统架构

### 架构图

<div align="center">
    <img src="docs/images/diagrams/system-architecture.png" alt="系统架构图" width="800"/>
</div>

### 技术架构

#### 前端架构

- 视图层
  - Vue 组件
  - Element UI
  - 自定义组件
- 数据层
  - Vuex 存储
  - LocalStorage
  - Cookie 管理
- 网络层
  - Axios 请求
  - WebSocket
  - 文件上传

#### 后端架构

- 应用层
  - 路由控制
  - 业务逻辑
  - 数据验证
- 服务层
  - 数据处理
  - 缓存服务
  - 任务队列
- 数据层
  - ORM 映射
  - 数据库操作
  - 数据缓存

### 数据库设计

#### 学生表设计

<div align="center">
    <img src="docs/images/diagrams/database-schema-students.png" alt="学生数据库设计" width="800"/>
</div>

字段说明：

- Sno: 学号(主键)
- Sname: 姓名
- Ssex: 性别
- Sage: 年龄
- Sdept: 院系
- Sclass: 班级
- Saddress: 地址

#### 教师表设计

<div align="center">
    <img src="docs/images/diagrams/database-schema-teachers.png" alt="教师数据库设计" width="800"/>
</div>

字段说明：

- Tno: 教师编号(主键)
- Tname: 教师姓名
- Tsex: 性别
- Tage: 年龄
- Tdept: 所属院系
- Ttitle: 职称
- Tphone: 联系电话

#### 课程表设计

<div align="center">
    <img src="docs/images/diagrams/database-schema-courses.png" alt="课程数据库设计" width="800"/>
</div>

字段说明：

- Cno: 课程号(主键)
- Cname: 课程名
- Ccredit: 学分
- Chour: 学时
- Cterm: 开课学期
- Cteacher: 授课教师
- Ctype: 课程类型

## 项目结构

```
student-management/
├── frontend/                # 前端代码
│   ├── public/             # 公共资源目录
│   │   ├── favicon.ico     # 网站图标
│   │   └── index.html      # HTML模板
│   ├── src/                # 源代码目录
│   │   ├── assets/         # 静态资源
│   │   │   ├── images/     # 图片资源
│   │   │   ├── styles/     # 样式文件
│   │   │   └── fonts/      # 字体文件
│   │   ├── components/     # 公共组件
│   │   │   ├── common/     # 通用组件
│   │   │   ├── layout/     # 布局组件
│   │   │   └── form/       # 表单组件
│   │   ├── views/          # 页面视图
│   │   │   ├── student/    # 学生相关页面
│   │   │   ├── teacher/    # 教师相关页面
│   │   │   └── course/     # 课程相关页面
│   │   ├── router/         # 路由配置
│   │   │   └── index.js    # 主路由文件
│   │   ├── store/          # Vuex状态管理
│   │   │   ├── modules/    # 状态模块
│   │   │   └── index.js    # 状态入口
│   │   ├── utils/          # 工具函��
│   │   │   ├── request.js  # axios封装
│   │   │   ├── auth.js     # 权限相关
│   │   │   └── validate.js # 验证工具
│   │   ├── api/            # API接口
│   │   │   ├── student.js  # 学生接口
│   │   │   ├── teacher.js  # 教师接口
│   │   │   └── course.js   # 课程接口
│   │   ├── App.vue         # 根组件
│   │   └── main.js         # 入口文件
│   ├── tests/              # 测试文件
│   │   ├── unit/          # 单元测试
│   │   └── e2e/           # 端到端测试
│   ├── package.json        # 项目依赖
│   ├── vue.config.js       # Vue配置
│   └── babel.config.js     # Babel配置
└── backend/                # 后端代码
    ├── app/               # Flask应用主目录
    │   ├── models/        # 数据模型
    │   │   ├── __init__.py
    │   │   ├── student.py # 学生模型
    │   │   ├── teacher.py # 教师模型
    │   │   └── course.py  # 课程模型
    │   ├── services/      # 业务逻辑
    │   │   ├── __init__.py
    │   │   ├── student.py # 学生服务
    │   │   ├── teacher.py # 教师服务
    │   │   └── course.py  # 课程服务
    │   ├── routes/        # 路由控制
    │   │   ├── __init__.py
    │   │   ├── student.py # 学生路由
    │   │   ├── teacher.py # 教师路由
    │   │   └── course.py  # 课程路由
    │   ├── utils/         # 工具函数
    │   │   ├── __init__.py
    │   │   ├── auth.py    # 认证工具
    │   │   ├── logger.py  # 日志工具
    │   │   └── response.py # 响应格式化
    │   ├── static/        # 静态文件
    │   └── templates/     # 模板文件
    ├── tests/             # 测试目录
    │   ├── __init__.py
    │   ├── test_models.py
    │   └── test_routes.py
    ├── config/           # 配置文件目录
    │   ├── __init__.py
    │   ├── development.py # 开发环境配置
    │   ├── production.py  # 生产环境配置
    │   └── testing.py    # 测试环境配置
    ├── logs/             # 日志目录
    ├── migrations/       # 数据库迁移
    ├── requirements.txt  # Python依赖
    ├── .env             # 环境变量
    ├── .gitignore       # Git忽略文件
    └── run.py           # 应用启动入口
```

### 目录说明

#### 前端结构（frontend/）

1. **public/** - 公共资源目录

   - 存放不需要经过 webpack 处理的静态资源
   - 包含网站图标和 HTML 模板文件

2. **src/assets/** - 静态资源目录

   - 存放项目所需的图片、样式、字体等资源
   - 这些资源会经过 webpack 处理和优化

3. **src/components/** - 组件目录

   - common/：通用组件，如按钮、表格等
   - layout/：布局组件，如头部、侧边栏等
   - form/：表单相关组件，如输入框、选择器等

4. **src/views/** - 页面视图目录

   - 按功能模块划分的页面组件
   - 包含学生、教师、课程等相关页面

5. **src/router/** - 路由配置

   - 定义应用的路由规则
   - 实现页面间的导航逻辑

6. **src/store/** - 状态管理

   - 使用 Vuex 管理应用状态
   - 按模块划分不同的状态管理逻辑

7. **src/utils/** - 工具函数目录

   - request.js：封装 axios 请求
   - auth.js：处理权限验证
   - validate.js：表单验证工具

8. **src/api/** - 接口目录

   - 按模块划分的 API 接口定义
   - 统一管理后端接口调用

#### 后端结构（backend/）

1. **app/models/** - 数据模型目录

   - 定义数据库表结构
   - 实现模型间的关联关系

2. **app/services/** - 业务逻辑目录

   - �� 装核心业务逻辑
   - 处理数据的增删改查操作

3. **app/routes/** - 路由控制目录

   - 处理 HTTP 请求
   - 调用相应的服务层方法

4. **app/utils/** - 工具函数目录

   - auth.py：用户认证相关
   - logger.py：日志记录工具
   - response.py：统一响应格式

5. **config/** - 配置文件目录

   - 不同环境的配置文件
   - 数据库、缓存等配置项

6. **tests/** - 测试目录

   - 单元测试和集成测试
   - 确保代码质量和功能正确性

7. **migrations/** - 数据库迁移目录

   - 管理数据库版本
   - 记录数据库结构变更

### 特点说明

1. **模块化设计**

   - 前后端代码完全分离
   - 功能模块清晰划分
   - 便于团队协作开发

2. **代码组织**

   - 遵循"关注点分离"原则
   - 采用 MVC 架构模式
   - 便于维护和扩展

3. **开发规范**

   - 统一的代码风格
   - 清晰的目录结构
   - 完整的文档注释

## 快速开始

### 环境要求

#### Python 环境

- Python 3.8+
  - pip 20.0+
  - virtualenv 20.0+
  - 必要的 Python 包:
    - Flask==2.0.1
    - SQLAlchemy==1.4.23
    - PyMySQL==1.0.2
    - Flask-CORS==3.0.10

#### Node 环境

- Node.js 14.0+
  - npm 6.14+
  - 必要的 Node 包:
    - vue@2.6.14
    - element-ui@2.15.6
    - axios@0.21.1

#### MySQL 环境

- MySQL 5.7+
  - 默认字符集：utf8mb4
  - 默认排序规则：utf8mb4_general_ci
  - 建议内存：4GB+
  - 建议存储空间：20GB+

### 详细安装步骤

1. **克隆项目**

```bash
# 克隆项目到本地
git clone [项目地址]
cd student-management

# 创建并切换到开发分支
git checkout -b dev
```

2. **后端环境配置**

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 检查安装
pip list
```

3. **前端环境配置**

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 检查安装
npm list
```

4. **数据库配置**

```bash
# 登录MySQL
mysql -u root -p

# 创建数据库
CREATE DATABASE sct CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

# 创建用户并授权
CREATE USER 'sct_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON sct.* TO 'sct_user'@'localhost';
FLUSH PRIVILEGES;

# 导入数据
mysql -u sct_user -p sct < sct.sql
```

5. **配置文件设置**

修改 `backend/config.py`：

```python
# 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql://sct_user:your_password@localhost/sct'

# 应用配置
DEBUG = True
SECRET_KEY = 'your-secret-key'

# 跨域配置
CORS_ORIGINS = ['http://localhost:8080']
```

6. **启动服务**

```bash
# 启动后端服务
cd backend
python run.py

# 启动前端服务
cd frontend
npm run serve
```

7. **访问系统**

- 前端开发服务器：http://localhost:8080
- 后端 API 服务器：http://localhost:5000

### 开发指南

#### 代码规范

- Python 代码遵循 PEP8 规范
- JavaScript 代码遵循 ESLint 规范
- CSS 采用 BEM 命名规范
- Git 提交信息规范化

#### 开发流程

1. 创建功能分支
2. 编写代码和测试
3. 提交代码审查
4. 合并到主分支

#### 测试要求

- 单元测试覆盖率>80%
- 集成测试覆盖主要功能
- 端到端测试确保功能完整

## 开发团队

### 核心开发者

- 后端开发：[曾毅]
  - 负责后端架构设计
  - API 接口开发
  - 数据库设计
- 前端开发：[曾毅]
  - 负责前端架构设计
  - 界面开发
  - 交互优化
- 数据库设计：[曾毅]
  - 数据库架构设计
  - 性能优化
  - 数据安全

## 版本历史

### v1.0.0 (2024-01-01)

- 初始版本发布
  - 完整的学生信息管理功能
    - 基础信息管理
    - 学籍管理
    - 成绩管理
  - 教师管理系统
    - 教师信息管理
    - 课程分配
    - 工资管理
  - 课程管理模块
    - 课程信息管理
    - 选课管理
    - 成绩管理

### v1.0.1 (2024-01-15)

- 功能优化
  - 优化查询性能
  - 改进用户界面
  - 修复已知问题
- 新增功能
  - 数据导出功能
  - 批量操作支持
  - 高级搜索功能

### v1.1.0 (计划中)

- 计划功能
  - 权限管理系统
  - 数据分析功能
  - 报表生成功能
- 技术升级
  - Vue 3 迁移
  - 微服务架构
  - 容器化部署

## 许可证

MIT License

Copyright (c) 2024 [曾毅]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[完整的 MIT 许可证内容...]

## 联系方式

### 技术支持

- 项目负责人：[曾毅]
- 邮箱：[3355262104@qq.com]
- QQ：3355262104
- 微信：zengyi3355262104

### 问题反馈

- Github Issues
- 邮件反馈
- QQ 群：[待创建]

## 致谢

特别感谢以下开源项目和团队：

- Vue.js 团队
  - 提供优秀的前端框架
  - 详细的开发文档
  - 活跃的社区支持
- Element UI 团队
  - 优秀的组件库
  - 完善的主题系统
  - 丰富的示例代码
- Flask 团队
  - 灵活的 Web 框架
  - 简洁的开发模式
  - 强大的扩展系统
- SQLAlchemy 团队
  - 强大的 ORM 框架
  - 优秀的查询构建器
  - 完善的文档支持

同时感谢所有为本项目提供建议和反馈的用户！
