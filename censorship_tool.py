# censorship_tool.py
import re

def censor_text(filename, bad_words):
    with open(filename, "r") as f:
        content = f.read()

    censored = content
    found = []

    for word in bad_words:
        pattern = re.compile(rf"\b{word}\b", re.IGNORECASE)
        matches = pattern.findall(content)
        if matches:
            found.extend(matches)
            censored = pattern.sub("***", censored)

    return found, censored


if __name__ == "__main__":
    file_name = input("Enter text file name: ")
    bad_words = ["badword", "ugly", "stupid"]  # add more as needed

    found, censored_output = censor_text(file_name, bad_words)

    print("\n=== Censorship Report ===")
    if found:
        print("Censored words:", set(found))
    else:
        print("No bad words found.")

    print("\n--- Censored Content ---")
    print(censored_output)

    # Save censored version
    with open("censored_output.txt", "w") as f:
        f.write(censored_output)
    print("\nCensored text saved to censored_output.txt")
