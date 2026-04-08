import os
from openai import OpenAI
from env.environment import ScamEnv
from env.models import Action

# ---------------------------
# ENV VARIABLES (REQUIRED)
# ---------------------------
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    HF_TOKEN = "dummy_key"

# Required by rules (even if not used)
client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)


# ---------------------------
# SMART RULE-BASED AGENT
# ---------------------------
def get_action(obs):
    msg = obs.message.lower()
    meta = obs.metadata if obs.metadata else {}
    history = obs.history if obs.history else []

    scam_keywords = [
        "otp", "money", "urgent", "verify",
        "bank", "upi", "link", "account",
        "suspended", "blocked", "click",
        "reward", "cashback", "offer", "win", "prize"
    ]

    # 🔴 STEP 1: First reaction
    if len(history) == 0:

        if any(word in msg for word in ["otp", "bank", "upi"]):
            return Action(
                action_type="report",
                response="This is a scam because it asks for OTP or banking details"
            )

        if any(word in msg for word in scam_keywords):
            return Action(
                action_type="warn_user",
                response="This message looks suspicious due to urgency or promotional scam patterns"
            )

        return Action(
            action_type="ignore",
            response="This appears to be a legitimate message"
        )

    # 🔵 STEP 2: Final decision (VERY IMPORTANT)
    else:

        if any(word in msg for word in scam_keywords):
            return Action(
                action_type="report",
                response="After analysis, this is confirmed to be a scam and should be reported"
            )

        if meta.get("sender") == "known_contact":
            return Action(
                action_type="verify_contact",
                response="Verify identity before taking action"
            )

        return Action(
            action_type="ignore",
            response="No strong scam signals after review"
        )


# ---------------------------
# RUN ENVIRONMENT
# ---------------------------
def run():
    env = ScamEnv()
    obs = env.reset()

    task_name = env.task["type"]

    print(f"[START] task={task_name} env=scamshield-openenv model={MODEL_NAME}")

    rewards = []
    step = 1
    done = False

    try:
        while not done:
            action = get_action(obs)

            obs, reward, done, info = env.step(action)

            rewards.append(f"{reward.score:.2f}")

            print(
                f"[STEP] step={step} action={action.action_type}('{action.response}') "
                f"reward={reward.score:.2f} done={str(done).lower()} error=null"
            )

            step += 1

        success = reward.score >= 0.5

    except Exception as e:
        print(f"[STEP] step={step} action=error reward=0.00 done=true error={str(e)}")
        success = False

    print(f"[END] success={str(success).lower()} steps={step-1} rewards={','.join(rewards)}")


if __name__ == "__main__":
    run()