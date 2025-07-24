# 🚀 AI-Powered Cold Email Automation Tool

An intelligent cold email automation system that generates personalized emails for job applications using OpenAI's GPT models. This tool researches companies, crafts tailored emails, and manages the entire email sending process with built-in safety features.

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Safety Features](#safety-features)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## ✨ Features

### 🤖 AI-Powered Email Generation
- **Intelligent Research**: Automatically visits company websites and "About Us" pages
- **Personalized Content**: Tailors each email based on company information
- **Professional Templates**: Generates subject lines and email bodies
- **Consistent Branding**: Maintains professional tone across all emails

### 📧 Smart Email Management
- **Duplicate Prevention**: Tracks sent emails to avoid duplicates
- **Backup System**: Saves generated emails for reuse and recovery
- **Batch Processing**: Handles multiple companies efficiently
- **Resume Attachment**: Automatically attaches your resume to each email

### 🛡️ Safety & Rate Limiting
- **Random Delays**: 15-20 minute delays between emails to avoid spam detection
- **Sent Email Tracking**: JSON-based tracking system
- **Error Handling**: Robust error handling and recovery
- **Gmail Integration**: Secure SMTP with app passwords

## 🔧 Prerequisites

- **Python 3.8+**
- **OpenAI API Account** with available credits
- **Gmail Account** with App Password enabled
- **CSV file** with company data

## 📦 Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd cold-mailer
```

2. **Install required packages**
```bash
pip install openai pandas python-dotenv
```

3. **Set up environment variables**
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=sk-your-openai-api-key-here
SENDER_EMAIL=your-email@gmail.com
EMAIL_APP_PASSWORD=your-gmail-app-password
RESUME_FILENAME=your-resume.pdf
CONTACT=+1234567890
LINKEDIN=https://linkedin.com/in/your-profile
```

## ⚙️ Configuration

### 1. OpenAI API Setup
- Visit [OpenAI Platform](https://platform.openai.com/api-keys)
- Create a new API key
- Add billing information (recommended: $5-10 budget)
- Copy the API key to your `.env` file

### 2. Gmail App Password
- Enable 2-Factor Authentication on your Gmail account
- Go to Google Account Settings → Security → App Passwords
- Generate a new app password for "Mail"
- Use this password in your `.env` file

### 3. Prepare Company Data
Create `resources/contacts.csv` with the following format:
```csv
Company,Email,Website
Google,careers@google.com,https://www.google.com
Microsoft,jobs@microsoft.com,https://www.microsoft.com
Apple,recruiting@apple.com,https://www.apple.com
```

### 4. Add Your Resume
Place your resume PDF in the `attachments/` folder and update the filename in `.env`

## 🚀 Usage

### Basic Usage
```bash
python mail_script.py
```

### What Happens When You Run It:

1. **📊 Data Loading**: Reads company data from CSV
2. **🔍 Backup Check**: Loads previously generated emails
3. **🤖 AI Generation**: Creates personalized emails for new companies
4. **📧 Email Sending**: Sends emails with random delays
5. **💾 Progress Tracking**: Updates sent email records

### Sample Output:
```
🔎 Companies already in backup: 5
🔎 Companies to generate: 3
✅ Parsed new GPT response.
✅ Backup file updated with new emails.
📧 Sending email to: careers@example.com (Company: Example Corp)
✅ Email sent to careers@example.com
⏳ Waiting 1150 seconds before next email...
```

## 📁 Project Structure

```
cold-mailer/
├── mail_script.py              # Main orchestrator script
├── .env                        # Environment variables
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── resources/
│   └── contacts.csv           # Company contact data
├── attachments/
│   └── resume.pdf             # Your resume file
├── helpers/
│   ├── __init__.py
│   ├── generate_email_drafts.py    # AI email generation
│   ├── send_email.py              # Email sending logic
│   ├── sent_mails.py              # Email tracking
│   ├── clean_json.py              # JSON response cleaning
│   ├── load_backup.py             # Backup management
│   └── segregate_companies.py     # Company filtering
├── gpt_email_response_backup.json  # Generated emails backup
└── sent_emails.json               # Sent email tracking
```

## 🛡️ Safety Features

### Rate Limiting
- **15-20 minute delays** between emails
- **Random intervals** to appear more human-like
- **Sent email tracking** prevents duplicates

### Error Handling
- **API quota management** with clear error messages
- **JSON parsing** with fallback handling
- **File backup** system for recovery

### Email Security
- **App passwords** instead of main Gmail password
- **SMTP SSL** encryption
- **Environment variable** protection

## 🔧 Troubleshooting

### Common Issues

**OpenAI API Quota Error**
```
Error: You exceeded your current quota
```
**Solution**: Add billing information or increase budget at [OpenAI Billing](https://platform.openai.com/account/billing)

**Gmail Authentication Error**
```
Error: Authentication failed
```
**Solution**: 
1. Enable 2FA on Gmail
2. Generate App Password
3. Use App Password in `.env` file

**Missing CSV File**
```
Error: File not found: resources/contacts.csv
```
**Solution**: Create the CSV file with Company, Email, Website columns

**Environment Variables Not Found**
```
Error: The api_key client option must be set
```
**Solution**: 
1. Check `.env` file exists
2. Verify `python-dotenv` is installed
3. Ensure `load_dotenv()` is called

### Debug Mode
Add debug prints to troubleshoot:
```python
print(f"API Key: {os.getenv('OPENAI_API_KEY')[:10]}...")
print(f"Email: {os.getenv('SENDER_EMAIL')}")
```

## 📊 Cost Estimation

### OpenAI API Costs (using gpt-4o-mini)
- **~$0.15 per 1M tokens**
- **~$0.01-0.05 per email** (depending on company research depth)
- **$5 budget** = ~100-500 emails

### Recommended Budget
- **Starter**: $5 (100+ emails)
- **Regular Use**: $10-20 (500+ emails)
- **Heavy Use**: $50+ (1000+ emails)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

- **Use responsibly**: Follow email best practices and anti-spam laws
- **Respect rate limits**: Don't overwhelm recipients
- **Personal use**: Intended for job searching and professional networking
- **No guarantees**: Success depends on email quality and recipient interest

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- Python community for excellent libraries
- Gmail for reliable SMTP services

---

**Happy Job Hunting! 🎯**

For questions or support, please open an issue in the repository.