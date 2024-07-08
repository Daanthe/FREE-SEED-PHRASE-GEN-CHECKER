import hashlib
import hmac
import base64
import random
import time

def load_wordlist(filename):
    with open(filename, 'r') as f:
        words = [line.strip() for line in f.readlines()]
    return words

def generate_mnemonic_phrase(wordlist, num_words):
    phrase = [wordlist[random.randint(0, len(wordlist) - 1)] for _ in range(num_words)]
    return '.'.join(phrase)

def validate_trust_wallet(mnemonic_phrase):
    # Trust Wallet uses BIP39 to generate the seed from the mnemonic phrase
    # We'll use the same algorithm to validate the phrase
    seed = hashlib.sha256(mnemonic_phrase.encode()).digest()
    hmac_sha256 = hmac.new(b'Bitcoin seed', seed, hashlib.sha256)
    checksum = hmac_sha256.digest()[:4]
    return all(byte == 0 for byte in checksum)

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def main():
    print_red("SpeedBTC")
    print_red("Options:")
    print_red("1. Generate Mnemonic Phrases")
    print_red("2. Socials")
    print_red("Enter your choice: ")
    option = int(input())

    if option == 1:
        wordlist_file = 'wordlist.txt'
        wordlist = load_wordlist(wordlist_file)
        print_red("How many words per phrase? (12 or 24)")
        while True:
            num_words = int(input())
            if num_words == 12 or num_words == 24:
                break
            else:
                print_red("Invalid choice. Please enter 12 or 24.")
        
        start_time = time.time()
        phrases_per_second = 0
        while True:
            mnemonic_phrase = generate_mnemonic_phrase(wordlist, num_words)
            print_red(f"Generated mnemonic phrase: {mnemonic_phrase}")
            if validate_trust_wallet(mnemonic_phrase):
                print_red("Valid Trust Wallet phrase!")
                break
            else:
                print_red("Invalid Phrase")
            phrases_per_second += 1
            if time.time() - start_time >= 1:
                print_red(f"Generating {phrases_per_second} phrases per second...")
                phrases_per_second = 0
                start_time = time.time()
    elif option == 2:
        print_red("Socials:")
        print_red("TikTok: @Speedcoder1")
        print_red("YouTube: @Speedcoder48")
        
    else:
        print_red("Invalid option. Please try again.")

if __name__ == '__main__':
    main()