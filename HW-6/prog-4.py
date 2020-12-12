import glob

print("Enter a path:", end="")
path = input().strip().rstrip('/')
print("Enter a filename:", end="")
filename = input().strip()

files = glob.glob(path + '/**/' + filename, recursive=True)
print(files[0])