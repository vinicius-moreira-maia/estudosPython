class Ordenador:
    def selection_sort(seq):
        fim = len(seq)

        for i in range(fim - 1):
            pos_do_menor = i

            # esse loop me garante que eu saiba a posição do menor elemento
            for j in range(i + 1, fim):
                if seq[j] < seq[pos_do_menor]:
                    pos_do_menor = j
            
            seq[i], seq[pos_do_menor] = seq[pos_do_menor], seq[i]  
        
    def bubble_sort(seq):
        ''' Implementação do curso da USP '''
        fim = len(seq)

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j+1], seq[j]
    
    def bubble(seq):
        ''' Implementação do programação Dinâmica '''
        fim = len(seq)

        for _ in range(fim - 1):
            for i in range(fim - 1):
                if seq[i] > seq[i + 1]:
                    seq[i], seq[i + 1] = seq[i+1], seq[i]
    
    def bubble_sort2(seq):
        ''' Implementação do curso da USP (versão melhorada) '''
        fim = len(seq)

        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j+1], seq[j]
                    trocou = True
            if not trocou:
               return

    def insertion_sort(lista):
        fim = len(lista)

        for i in range(1, fim):
            chave = lista[i]

            j = i - 1

            while j >= 0 and lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
            
            lista[j + 1] = chave

if __name__ == '__main__':
    ...
