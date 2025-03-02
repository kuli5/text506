# AI驱动的Meme币分析工具 - 开发基础文档（Windows版）

## 项目概述
目标：开发一个Web工具，利用AI分析meme币的社交媒体情绪和链上数据，提供趋势洞察。  
MVP功能：输入meme币名称，展示X平台情绪评分和交易量趋势。

---

## 1. 软件需求
以下是开发所需的软件，确保在Windows上安装最新版本。

### 1.1 基础工具
- **VS Code**：代码编辑器  
  - 下载：https://code.visualstudio.com/  
  - 安装：运行安装程序，选择“添加到PATH”。  
  - 推荐插件：Prettier（代码格式化）、Python、ESLint。  
- **Chocolatey**：Windows包管理器（可选，类似Homebrew）  
  - 安装命令（以管理员身份运行PowerShell）：  
    ```powershell
    Set-ExecutionPolicy Bypass -Scope CurrentUser -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    ```  
  - 验证：`choco --version`  

### 1.2 开发环境
- **Node.js**：前端和后端运行时  
  - 下载：https://nodejs.org/（选择LTS版本）  
  - 安装：运行安装程序，勾选“Add to PATH”。  
  - 验证：打开CMD，输入`node -v`（建议v16或以上）。  
- **Python**：AI和数据处理  
  - 下载：https://www.python.org/downloads/（建议3.9+）  
  - 安装：运行安装程序，勾选“Add Python to PATH”。  
  - 验证：CMD输入`python --version`或`python3 --version`。  
- **Git**：版本控制  
  - 下载：https://git-scm.com/download/win  
  - 安装：运行安装程序，选择“Use Git from the Windows Command Prompt”。  
  - 验证：CMD输入`git --version`。  

### 1.3 依赖库
- **前端**：  
  - React：`npm install -g create-react-app`  
  - Axios（API请求）：`npm install axios`  
- **后端/AI**：  
  - Flask：`pip install flask`  
  - Tweepy（X API）：`pip install tweepy`  
  - TextBlob（情绪分析）：`pip install textblob`  
  - Requests（HTTP请求）：`pip install requests`  
  - Pandas（数据处理）：`pip install pandas`  
  - Scikit-learn（机器学习）：`pip install scikit-learn`  

---

## 2. 环境配置
在Windows上配置开发环境，分前端、后端和AI模块。

### 2.1 前端环境
1. 创建React项目：  
   ```cmd
   npx create-react-app meme-coin-frontend
   cd meme-coin-frontend
   npm start

2. 验证：浏览器打开http://localhost:3000，看到React默认页面。

## 2.2 后端环境

### 创建后端文件夹
```cmd
mkdir meme-coin-backend
cd meme-coin-backend
```

### 创建虚拟环境
```cmd
python -m venv venv
venv\Scripts\activate
```

（激活后命令行前会出现 `(venv)`）

### 安装依赖
```cmd
pip install flask tweepy textblob requests
```

### 创建简单后端文件 `app.py`
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Meme Coin!"

if __name__ == "__main__":
    app.run(debug=True)
```

### 运行后端
```cmd
python app.py
```

访问 [http://localhost:5000](http://localhost:5000) 测试。

## 2.3 数据/AI 环境

### 在 `meme-coin-backend` 中测试 Python 库

创建 `test.py`：
```python
from textblob import TextBlob
text = "I love Dogecoin!"
blob = TextBlob(text)
print(blob.sentiment.polarity)  # 输出情绪得分
```

### 运行测试
```cmd
python test.py
```

## 2.4 API 密钥

### X API（Twitter）
1. **申请**：[Twitter Developer](https://developer.twitter.com/)
2. **创建开发者账户**，选择 `Hobbyist` 或 `Business`，填写用途。
3. **创建项目**，如 `MemeCoinSentiment`，选择 `Exploring the API`。
4. **创建 Twitter 应用**，命名 `MemeCoinAnalysis`。
5. **获取 API Key、Secret、Bearer Token**：
   - 进入 **Developer Portal** > **Projects & Apps**。
   - 选择你的应用，进入 **Keys and Tokens** 选项卡。
   - 生成 `API Key`、`API Secret` 和 `Bearer Token`。
6. **保存 API 密钥**
   在 `meme-coin-backend/.env` 文件中添加：
   ```env
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_BEARER_TOKEN=your_bearer_token
   ```
7. **安装 `python-dotenv` 以加载环境变量**：
   ```cmd
   pip install python-dotenv
   ```

### CoinGecko API
无需密钥，直接使用。

## 3. Git 版本控制
使用 Git 管理代码，确保开发过程可追溯。

### 3.1 初始化 Git

在项目根目录（新建 `meme-coin-analysis` 文件夹）：
```cmd
mkdir meme-coin-analysis
cd meme-coin-analysis
git init
```

### 配置 Git
```cmd
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 3.2 项目结构
```
meme-coin-analysis/
├── meme-coin-frontend/  # React 前端
├── meme-coin-backend/   # Flask 后端和 AI
├── .gitignore           # 忽略文件
└── README.md            # 项目说明
```

### 创建 `.gitignore`
```cmd
echo node_modules/ > .gitignore
echo venv/ >> .gitignore
echo *.pyc >> .gitignore
echo .env >> .gitignore
```

### 3.3 提交代码

#### 添加文件
```cmd
git add .
```

#### 提交更改
```cmd
git commit -m "Initial commit with frontend and backend setup"
```

#### 创建远程仓库（GitHub）

在 GitHub 上新建仓库 `meme-coin-analysis`。

#### 推送代码
```cmd
git remote add origin https://github.com/your-username/meme-coin-analysis.git
git branch -M main
git push -u origin main
```

### 3.4 开发流程

#### 创建新功能分支
```cmd
git checkout -b feature/sentiment-analysis
```

#### 提交更改
```cmd
git add .
git commit -m "Add sentiment analysis with TextBlob"
git push origin feature/sentiment-analysis
```

#### 合并到主分支
```cmd
git checkout main
git merge feature/sentiment-analysis
git push origin main
```

## 4. 开发注意事项
- **时间管理**：每天 `7-9 点` Coding，`9-11 点` 测试和 Git 提交。
- **依赖更新**：定期运行 `npm update` 和 `pip install --upgrade <package>`。
- **备份**：Git 推送到远程仓库，避免本地数据丢失。

## 5. 下一步
- 实现 **X 情绪分析** 和 **CoinGecko 数据获取**（参考后续文档）。
- 开发 **前端仪表盘** 展示分析结果。

**请将此文档保存到 `meme-coin-analysis/README.md`，并随时更新！**

