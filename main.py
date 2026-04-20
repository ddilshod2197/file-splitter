def fayl_bo'laklarga_ajratish(fayl_nomi, bo'lak_hajmi):
    try:
        with open(fayl_nomi, 'r') as f:
            fayl_mahsuloti = f.read()
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return

    bo'laklar_soni = len(fayl_mahsuloti) // bo'lak_hajmi
    qolgan_qismi = len(fayl_mahsuloti) % bo'lak_hajmi

    with open(fayl_nomi + "_bo'lak_1.txt", 'w') as f:
        f.write(fayl_mahsuloti[:bo'lak_hajmi])

    for i in range(2, bo'laklar_soni + 1):
        with open(fayl_nomi + "_bo'lak_" + str(i) + ".txt", 'w') as f:
            f.write(fayl_mahsuloti[(i - 1) * bo'lak_hajmi:i * bo'lak_hajmi])

    if qolgan_qismi != 0:
        with open(fayl_nomi + "_bo'lak_" + str(bo'laklar_soni + 1) + ".txt", 'w') as f:
            f.write(fayl_mahsuloti[bo'laklar_soni * bo'lak_hajmi:])

fayl_bo'laklarga_ajratish("fayl.txt", 100)
```

```python
import os

def fayl_bo'laklarga_ajratish(fayl_nomi, bo'lak_hajmi):
    try:
        with open(fayl_nomi, 'r') as f:
            fayl_mahsuloti = f.read()
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return

    bo'laklar_soni = len(fayl_mahsuloti) // bo'lak_hajmi
    qolgan_qismi = len(fayl_mahsuloti) % bo'lak_hajmi

    for i in range(1, bo'laklar_soni + 2):
        with open(fayl_nomi + "_bo'lak_" + str(i) + ".txt", 'w') as f:
            if i == 1:
                f.write(fayl_mahsuloti[:bo'lak_hajmi])
            elif i == bo'laklar_soni + 1:
                f.write(fayl_mahsuloti[bo'laklar_soni * bo'lak_hajmi:])
            else:
                f.write(fayl_mahsuloti[(i - 1) * bo'lak_hajmi:i * bo'lak_hajmi])

    os.remove(fayl_nomi)

fayl_bo'laklarga_ajratish("fayl.txt", 100)
