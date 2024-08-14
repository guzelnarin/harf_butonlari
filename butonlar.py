import tkinter as tk

root = tk.Tk()
root.title("Metni Büyük Harfe Çevirme")
root.state("zoomed")



def reset():
    text.delete(1.0, tk.END)
    text2.delete(1.0, tk.END)
    text3.delete(1.0, tk.END)
    text4.delete(1.0, tk.END)
    text5.delete(1.0, tk.END)



def buyut():
    input_text = text.get("1.0", tk.END).strip()
    upper_text =  ""
    for harf in input_text:
      if harf == 'ı':
          upper_text+='I'
      elif harf == 'i':
          upper_text+='İ'     
      elif harf == 'u':
          upper_text+='U'
      elif harf == 'ü':
          upper_text+='Ü'            
      elif harf == 'ö':
          upper_text+='Ö'
      elif harf == 'o':
          upper_text+='O'
      else:
          upper_text+=harf.upper()  


    text2.insert(tk.END, upper_text)


def turkce_harfler(char):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    
    # Karakteri alfabe içinde bul ve sıralama için indeksini döndür
    if char == 'İ':
        char = 'i'
    elif char == 'I':
        char = 'ı'
    lower_char = char.lower() 
    if lower_char in alfabe:
        return alfabe.index(lower_char)
    else:
        return len(alfabe)

def harf_sirala():
    metin = text.get("1.0", tk.END).strip()
    metin_list = list(metin)
    N = len(metin_list)
    
    for i in range(N):
        for j in range(0, N - 1):
            if turkce_harfler(metin_list[j]) > turkce_harfler(metin_list[j + 1]):
                metin_list[j], metin_list[j + 1] = metin_list[j + 1], metin_list[j]
    
    sorted_text = ''.join(metin_list)
    text3.delete("1.0", tk.END) 
    text3.insert(tk.END, sorted_text)



def harfleri_ayir():
    harfler = text.get("1.0", tk.END).strip()
    sesli_harfler = "aeıioöuüAEIİOÖUÜ"    
    sesli=""
    sessiz=""

    for harf in harfler:
        if harf in sesli_harfler:
            sesli += harf

        else:
            sessiz += harf
            

    text4.insert(tk.END, sesli)        
    text5.insert(tk.END,sessiz)       
   
  


text = tk.Text(root,bg='light green',height=2,width=25)
text.place(x=250,y=25)

text2 = tk.Text(root,bg='light gray',height=2,width=25)
text2.place(x=250,y=70)

text3 = tk.Text(root, bg='light blue',height=2,width=25 )
text3.place(x=250,y=115)

text4 = tk.Text(root,bg='yellow',height=2,width=25)
text4.place(x=250,y=160)

text5 = tk.Text(root, bg='orange',height=2,width=25)
text5.place(x=460,y=160)


button = tk.Button(root,background='green',text="<<",font=("Helvetica", 13, "bold"),command=buyut,activebackground='green',borderwidth=0)
button.place(x=460,y=25)

button_reset = tk.Button(root,bg='red', text='X',font=("Helvetica", 13, "bold") ,width=2,height=1,command=reset,activebackground='red',borderwidth=0)
button_reset.place(x=555,y=25)

button_harf_sirala = tk.Button(root, bg='blue',text='<=',font=("Helvetica", 13, "bold") ,width=2,height=1,command=harf_sirala,activebackground='blue',borderwidth=0)
button_harf_sirala.place(x=495,y=25)

button_harfleri_ayir = tk.Button(root, bg='grey' , text="<>",font=("Helvetica", 13, "bold") ,width=2,height=1,command=harfleri_ayir,activebackground='grey',borderwidth=0)
button_harfleri_ayir.place(x=525,y=25)





























root.mainloop()