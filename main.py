text = "X-DSPAM-Confidence:    0.8475"
start = text.find("0")
end = text.find("5")
total = text[start:]
print(total)
# for the exercise I needed the float, but for python you don't need.
whole = float(str(total))
print(whole)
