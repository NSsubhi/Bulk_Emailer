import json
import os
from openai import OpenAI
from helpers.clean_json import clean_gpt_json

def generate_email_drafts(companies_to_generate, backup_dict, backup_file):
    if not companies_to_generate:
        print("✅ All companies already have email drafts in backup.")
        return backup_dict

    # Get contact info from environment variables
    contact_number = os.getenv("CONTACT")
    linkedin_url = os.getenv("LINKEDIN")

    prompt = f"""
    You are a professional email writer. 
    
    For each company below, generate a tailored email introducing myself as a graduate student from NYU currently pursuing my MS in CS looking for software development roles. 

    Visit the website of the company, see what they do and tailor the mail accordingly.

    Navigate to the about us section in the company's website if it exists, in order to gather more information about the company.

    In the mail write a few sentences in a way such that the mail gives a personal touch (you can do this using the information gained through the company website and the about us page).

    In the salutation, just put "Hello," and nothing else.
    
    Mention that I'm a Software Engineer with 2+ years of experience at Oracle, where I developed scalable Supply Chain Management solutions for 40,000+ global customers using Java, Spring Boot, and Oracle DB. I'm currently exploring new SDE opportunities. 
    I have software development experience with Spring Boot, Node.js, React and Next.js and hands-on project experience in machine learning, data science and AI (Scikit-Learn, TensorFlow, PyTorch, LLMs, RAG), and would love to work for their organization. 
    
    Say I am attaching my resume and would appreciate any help.

    End the email with:
    
    Best regards,
    Subhiksha Seshadri
    
    Contact: {contact_number}
    LinkedIn: {linkedin_url}

    Return ONLY a valid JSON object, where each key is the company name and the value is another JSON object with:

    - "subject": the email subject line
    - "body": the full email body (excluding the subject)

    Return ONLY a strict JSON object with no markdown formatting or code fences.

    Make the mail concised and reader friendly. 

    Companies:

    {companies_to_generate}
    """

    # Initialize OpenAI client
    client = OpenAI()

    # Call GPT
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional email writer and return JSON only."},
            {"role": "user", "content": prompt}
        ]
    )

    # Clean and parse response
    email_json_text = clean_gpt_json(response.choices[0].message.content)

    try:
        new_emails = json.loads(email_json_text)
        print("✅ Parsed new GPT response.")
    except json.JSONDecodeError as e:
        print("❌ Failed to parse GPT output:", e)
        new_emails = {}

    # Update backup dict and write to file
    backup_dict.update(new_emails)
    with open(backup_file, "w") as f:
        json.dump(backup_dict, f, indent=2)
    print("✅ Backup file updated with new emails.")

    return backup_dict
