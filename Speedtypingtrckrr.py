import time

def calculate_accuracy(original, typed):
    correct = 0
    for o, t in zip(original, typed):
        if o == t:
            correct += 1
    return (correct / len(original)) * 100


def main():
    print("=== Typing Speed Tester ===\n")

    sentence = "When Sayooj and Nithul came to college Jaswin also arrived and Jaswin fell in a mud pit."
    print("Type this sentence:\n")
    print(sentence)

    input("\nPress Enter when ready...")

    start_time = time.time()
    typed = input("\nStart typing:\n")
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(sentence.split())

    speed = (words / time_taken) * 60
    accuracy = calculate_accuracy(sentence, typed)

    print(f"\nTime Taken: {round(time_taken, 2)} seconds")
    print(f"Typing Speed: {round(speed, 2)} WPM")
    print(f"Accuracy: {round(accuracy, 2)}%")

if __name__ == "__main__":
    main()
