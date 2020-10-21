import sys
import time
import random
import datetime
import os

from time import sleep

class GenerateFamilyDoc:

    def __init__(self, familyName, visitDate, noChildren):
        self.m_familyName = familyName
        self.m_visitDate = visitDate
        self.m_fileName = '2020_12_0' + str(visitDate) + '__' + familyName
        self.m_totalNoChildren = noChildren
        self.m_pageBrakeAfterChild = []
        self.m_pageNo = 1
        print('--- ' + str(self.m_totalNoChildren) + ' ---------------------')

    def generate(self):
        if 0 == self.m_totalNoChildren:
            return -1
        elif 1 == self.m_totalNoChildren:
            self.__prepare(1)
            return 1
        else:
            for child in range(self.m_totalNoChildren - 1):
                print('No child: ' + str(child+1) + ' and ' + str(child+2))
                p1 = self.__prepare(child+1)
                p2 = self.__prepare(child+2)
                if ( p1 != p2):
                    self.m_pageBrakeAfterChild.append(child + 1)
            self.__prepare(self.m_totalNoChildren)

    def __prepare(self, noChilds):
        self.__prepareDoc()
        for c in range(noChilds):
            print ('ccccccccccccccccccc: ' + str(c))
            self.__addChild()
            self.__pageBreak(c + 1)
        self.__finalizeDoc()
        self.__generatePdf()
        return self.__getNumberOfPagesPDF()

    def __prepareDoc(self):
        text=str(
            '\\documentclass[12pt, a4paper, oneside, draft]{article}\n\n' +
            '\\usepackage[a4paper]{geometry}\n' +
            '\\usepackage[utf8]{inputenc} % this is needed for umlauts\n' +
            '\\usepackage[ngerman]{babel} % this is needed for umlauts\n' +
            '\\usepackage[T1]{fontenc}    % this is needed for correct output of umlauts in\n' +
            '\\usepackage{float}\n' +
            '\\usepackage{tabularx}       % Automatic multirow tables\n\n' +
            '\\begin{document}\n')
        fileHdl = open(self.m_fileName + '.tex', 'w')
        fileHdl.write(text)
        fileHdl.close()

    def __addChild(self):
        kind1=str('\section{Prozessor auswaehlen}\n' +
                  'Ich wollte den Prozessor nicht direkt aufs Board layouten. Das habe ich mir fuer den ersten Schritt nicht zugetraut. Aus EMV-Gruenden (Elektro Magnetische Vertraeglichkeit) ist das nicht ganz einfach und braucht etwas Erfahrung. Deswegen habe ich ein Eval-Board gekauft. Dort ist der Prozessor vernuenftig eingebaut. Preis pro Stueck, weniger als 1\$.\n\n' +
                  'Ich wollte den Prozessor nicht direkt aufs Board layouten. Das habe ich mir fuer den ersten Schritt nicht zugetraut. Aus EMV-Gruenden (Elektro Magnetische Vertraeglichkeit) ist das nicht ganz einfach und braucht etwas Erfahrung. Deswegen habe ich ein Eval-Board gekauft. Dort ist der Prozessor vernuenftig eingebaut. Preis pro Stueck, weniger als 1\$.\n\n' +
                  'Ich wollte den Prozessor nicht direkt aufs Board layouten. Das habe ich mir fuer den ersten Schritt nicht zugetraut... xxxxxxxxxxxxxxxxxx ssssssssssssssss ssssssssssssssssss ssssssssssssssss \n\n')
        fileHdl = open(self.m_fileName + '.tex', 'a')
        fileHdl.write('\n')
        fileHdl.write(kind1)
        fileHdl.close()

    def __pageBreak(self, child):
        if child in self.m_pageBrakeAfterChild:
            pageBreak='\n\pagebreak\n'
            fileHdl = open(self.m_fileName + '.tex', 'a')
            fileHdl.write(pageBreak)
            fileHdl.close()

    def __finalizeDoc(self):
        endOfDoc='\n\n\end{document}\n'
        fileHdl = open(self.m_fileName + '.tex', 'a')
        fileHdl.write(endOfDoc)
        fileHdl.close()

    def __generatePdf(self):
        os.system('pdflatex ' + self.m_fileName + '.tex 2>&1 ' + self.m_fileName + '.lll')
        os.system('rm -f ' + self.m_fileName + '.aux')
        os.system('rm -f ' + self.m_fileName + '.log')
        os.system('rm -f ' + self.m_fileName + '.out')
        #os.system('rm -f ' + self.m_fileName + '.tex')

    def __getNumberOfPagesPDF(self):
        cmd = "pdfinfo " + self.m_fileName + ".pdf | grep 'Pages' | awk '{print $2}'"
        noPages = os.popen(cmd).read().strip()
        print('No pages: ' + str(noPages))
        return noPages


#    myPdfReader = pyPdf.PdfFileReader(open(docName + '.pdf'))
#    noPages = myPdfReader.getNumPages()
#    print('No pages: ' + str(noPages))


print('Generate Chlaus Documents')
print('  V00.01')

os.system('rm -f *~')


fam1 = GenerateFamilyDoc('Muster_c1', 5, 1)
fam1.generate()

fam2 = GenerateFamilyDoc('Muster_c2', 5, 2)
fam2.generate()

fam3 = GenerateFamilyDoc('Muster_c3', 6, 3)
fam3.generate()

fam4 = GenerateFamilyDoc('Muster_c17', 6, 17)
fam4.generate()
