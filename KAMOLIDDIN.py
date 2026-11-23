# class odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#     def salomlash(self):
#         print("Salom, mening ismim " + self.ism)
# p1 = odam("Kamoliddin", 17)
# p1.salomlash()
#
#
#
# class odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
# p1 = odam("Kamoliddin", 17)
# print(p1.ism)
# print(p1.yosh)
#
#
#
# p1 = odam("Kamoliddin", 17)
# print(p1.ism)
#
#
#
# class odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
# p1 = odam("Kamoliddin", 17)
# print(p1.ism)
# print(p1.yosh)
#
#
#
# class odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
# p1 = odam("Email")
# p2 = odam("Kamoliddin", 17)
# print(p1.ism, p1.yosh)
# print(p2.ism, p2.yosh)
#
#
#
# class odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#
#     def salomlash(self):
#         print("Salom, mening ismim " + self.ism)
# p1 = odam("Kamoliddin", 17)
# p1.salomlash()
#
#
#
#
# class odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
# p1 = odam("Kamoliddin", 17)
# print(p1.ism)
# print(p1.yosh)
#
#
#
# p1 = odam("Kamoliddin", 17)












#
# import docx
# import openpyxl
#
# print(" python-docx versiyasi:", docx.__version__ )
# print(" openpyxl versiyasi:", openpyxl.__version__)
# print(" Hammmasi tayyor!")
#
# from docx import Document
# doc = Document()
# doc.add_heading('Mening birinchi hujjatim', level=0)
# doc.add_heading('Kirish qismi', level=1)
# doc.add_paragraph('Bu paragraph oddiy mayn. Istalgan uzunlikda yozsa bo\'ladi.')
# doc.add_paragraph('Bu ikkinchi psragraf. Har bir add_paragraph yangi yaratadii.')
# doc.save('ksdffhkj.docx')
# print('Fayl yaratadi: birinchi_hujjat.docx')

# from docx import Document
# from docx.shared import Pt, RGBColor
# doc = Document()
# doc.add_heading('Shrift namunalari', level=1)
# p = doc.add_paragraph()
# r1 = p.add_run('Oddiy matn.   ')
# r2 = p.add_run('Bu qalin matn')
# r2.bold = True
# r3 = p.add_run('Bu kursiv matn.  ')
# r3.italic=True
# r4 = p.add_run('Tagiga chizilgan')
# r4.underline = True
# p2 = doc.add_paragraph()
# r5 = p2.add_run(' Bu 18pt qizil matn!.')
# r5.font.size=Pt(18)
# r5.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)
# r6=p2.add_run('Bu 14pt ko\'k matni')
# r6.font.size=Pt(14)
# r6.font.color.rgb = RGBColor(0x00, 0x70, 0xC0)
# doc.save('word_shrift.docx')
# print('word_shrift.docx saqlamdi')


# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# ws.title="O'quvchilar"
# ws['A1']='№'
# ws['B1']='Ism'
# ws['C1']=
