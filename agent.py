# agent.py
import datetime

def generate_post():
    """Agent's planning step"""
    today = datetime.date.today().strftime("%B %d, %Y")
    return f"Daily AI update on {today}: Building automation with Agentic AI. #AI #automation"

def post_to_linkedin(content):
    """Agent's acting step (mock for now)"""
    print(f"[ACTION] Would post to LinkedIn: {content}")

def observe_and_learn(success=True):
    """Agent's observing step"""
    if success:
        print("[OBSERVE] Post successful ✅")
    else:
        print("[OBSERVE] Post failed ❌ — will retry")

def run_agent():
    post = generate_post()
    post_to_linkedin(post)
    observe_and_learn(True)

if __name__ == "__main__":
    run_agent()
