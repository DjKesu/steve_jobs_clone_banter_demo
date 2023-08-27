from gptTextConversation import createConversation
from audioInput import speech_to_text

def main():
    while True:
        speaker2_text = speech_to_text()
        if speaker2_text:
            createConversation(speaker2_text)

if __name__ == "__main__":
    main()
