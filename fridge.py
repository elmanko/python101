from contextlib import closing
class RefrigeratonRaider:

    def open(self):
        print('abrio refrigerador')

    def take(self, food):
        print(f'buscando {food}...')
        if food == 'pizza':
            raise RuntimeError('Ponte a dieta cerdo')
        print(f'tomando {food}')
    
    def close(self):
        print(f'cerrando refri alv')
    
def raid(food):
    with closing(RefrigeratonRaider()) as r:
        r = RefrigeratonRaider()
        r.open()
        r.take(food)
        #r.close()