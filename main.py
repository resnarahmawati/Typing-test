from time import time

#Menghitung keakuratan prompt input
def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# Menghitung kecepatan dalam kata per menit
def typingSpeed(iprompt, stime, etime):
    global time
    global iwords

    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time

    return speed

# Menghitung total waktu yang telah dilalui
def timeElapsed(stime, etime):
    time = etime - stime 

    return time

name = input('Masukkan Nama kamu: ')
if __name__ == '__main__':
    prompt = 'Saya adalah seorang programmer junior yang sedang membuat project.'
    print("Type this:-", prompt,)

    input("Klik ENTER jika kamu siap!")

    stime = time()
    iprompt = input()
    etime = time()

    # Mengumpulkan semua informasi yang dikembalikan dari fungsi- fungsi
    time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    # Menampilkan semua data ke console
    print("Total waktu : ", time, "Detik")
    print("Rata-rata KEcepatan mengetik kamu adalah : ", speed, "WPM")
    print("total : ", errors, "errors/typo")