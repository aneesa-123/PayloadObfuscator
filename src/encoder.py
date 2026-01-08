import base64, random, string, argparse, codecs

def base64_encode(data):
    return base64.b64encode(data.encode()).decode()


def base64_decode(data):
    return base64.b64decode(data.encode()).decode()


def xor_encode(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def rot13(data):
    return codecs.encode(data, 'rot_13')

def random_insert(data, count=3):
    out = list(data)
    for _ in range(count):
       idx = random.randrange(len(out)+1)
       out.insert(idx, random.choice(string.ascii_letters))
    return ''.join(out)

def escape_obfuscate(data):
    return ''.join(f"\\x{ord(c):02x}" for c in data)

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Payload Encoder & Obfuscation")
   parser.add_argument("payload", help="String payload to transform")
   args = parser.parse_args()

   original = args.payload
   b64 = base64_encode(original)
   xor = xor_encode(original, "k")
   rot = rot13(original)
   ins = random_insert(original)
   esc = escape_obfuscate(original)

   print("Original:", original)
   print("Base64:", b64)
   print("XOR Encoded:", xor)
   print("ROT13:", rot)
   print("Random Insert:", ins)
   print("Escape Obfus.:", esc)


#Evasion Testing 

print("\nEvasion Detection Results")
signatures = ["mal", "exec", "cmd", "shell"]

def detect(payload):
    return any(sig in payload for sig in signatures)

for label, data in [
        ("Original", original),
        ("Base64", b64),
        ("XOR", xor),
        ("ROT13", rot),
        ("RandomInsert", ins),
        ("Escaped", esc)]:
     detected = "Detected" if detect(data) else "Not Detected"
     print(f"{label}: {detected}")



with open("outputs/results.txt","w") as f:
   f.write(f"Original: {original}\nBase64: {b64}\n...")






