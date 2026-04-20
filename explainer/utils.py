import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')
def detect_language(error_text):
    """Detect programming language from error text"""
    error_lower = error_text.lower()
    if 'traceback' in error_lower or 'python' in error_lower:
        return 'Python'
    elif 'typeerror' in error_lower or 'undefined' in error_lower or 'null' in error_lower:
        return 'JavaScript'
    elif 'nullpointerexception' in error_lower or 'java' in error_lower:
        return 'Java'
    elif 'syntaxerror' in error_lower and 'php' in error_lower:
        return 'PHP'
    else:
        return 'Unknown'

def detect_severity(error_text):
    """Detect severity from error text"""
    error_lower = error_text.lower()
    if 'warning' in error_lower:
        return 'Warning'
    elif 'critical' in error_lower or 'fatal' in error_lower:
        return 'Critical'
    else:
        return 'Error'

def explain_error(error_text):
    """Send error to Gemini and get explanation"""
    prompt = f"""
    You are an expert programming assistant. Analyze this error and provide:
    
    1. **What happened** - Plain English explanation (2-3 sentences max)
    2. **Root Cause** - Why did this error occur?
    3. **Fix** - Exact steps to fix it with code example
    4. **Pro Tip** - One tip to avoid this in future
    
    Keep it beginner friendly. No jargon.
    
    Error:
    {error_text}
    """
    response = model.generate_content(prompt)
    return response.text