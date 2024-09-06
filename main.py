from dotenv import load_dotenv
from langchain.agents import tool
load_dotenv()

@tool
def get_name_len(text: str) -> int:
    """Returns the length of a text by characters"""
    return len(text)


if __name__ == "__main__":
    print("HELLO REACT LANGCHAIN")
    print(get_name_len(text="Dong"))
