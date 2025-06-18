class Paragem:
    def __init__(self, nome, lat, lng):
        self.nome = nome
        self.lat = lat
        self.lng = lng
        self.ligacoes = []

class Ligacao:
    def __init__(self, carreira, origem, destino, custo, tempo):
        self.carreira = carreira
        self.origem = origem
        self.destino = destino
        self.custo = custo
        self.tempo = tempo

class Carreira:
    def __init__(self, nome):
        self.nome = nome
        self.paragens = []
        self.custo_total = 0.0
        self.tempo_total = 0.0

class SistemaTransporte:
    def __init__(self):
        self.carreiras = []
        self.paragens = []
    
    def adicionar_carreira(self, nome):
        if not any(c.nome == nome for c in self.carreiras):
            self.carreiras.append(Carreira(nome))
            return True
        return False
    
    def adicionar_paragem(self, nome, lat, lng):
        if not any(p.nome == nome for p in self.paragens):
            self.paragens.append(Paragem(nome, lat, lng))
            return True
        return False
    
    def adicionar_ligacao(self, nome_carreira, nome_origem, nome_destino, custo, tempo):
        if custo < 0 or tempo < 0:
            return "Custo ou tempo negativo"
        
        carreira = next((c for c in self.carreiras if c.nome == nome_carreira), None)
        origem = next((p for p in self.paragens if p.nome == nome_origem), None)
        destino = next((p for p in self.paragens if p.nome == nome_destino), None)
        
        if not carreira:
            return "Carreira não existe"
        if not origem or not destino:
            return "Paragem não existe"
        
        # Verifica se a ligação é válida (origem ou destino devem ser extremidades)
        if carreira.paragens:
            if nome_origem != carreira.paragens[-1].nome and nome_destino != carreira.paragens[-1].nome:
                return "Ligação não conectada"
        
        ligacao = Ligacao(carreira, origem, destino, custo, tempo)
        origem.ligacoes.append(ligacao)
        
        if not carreira.paragens:
            carreira.paragens.append(origem)
        carreira.paragens.append(destino)
        
        carreira.custo_total += custo
        carreira.tempo_total += tempo
        
        return "Ligação adicionada"
    
    def listar_carreiras(self):
        for carreira in self.carreiras:
            if carreira.paragens:
                origem = carreira.paragens[0].nome
                destino = carreira.paragens[-1].nome
                print(f"{carreira.nome} {origem} {destino} {len(carreira.paragens)} {carreira.custo_total:.2f} {carreira.tempo_total:.2f}")
            else:
                print(f"{carreira.nome} 0 {carreira.custo_total:.2f} {carreira.tempo_total:.2f}")
    
    def listar_paragens(self, nome_carreira=None, inverso=False):
        if nome_carreira:
            carreira = next((c for c in self.carreiras if c.nome == nome_carreira), None)
            if carreira:
                paragens = carreira.paragens[::-1] if inverso else carreira.paragens
                print(", ".join(p.nome for p in paragens))
        else:
            for paragem in self.paragens:
                num_carreiras = sum(1 for c in self.carreiras if any(p.nome == paragem.nome for p in c.paragens))
                print(f"{paragem.nome}: {paragem.lat:.12f} {paragem.lng:.12f} {num_carreiras}")
    
    def intersecoes(self):
        for paragem in self.paragens:
            carreiras = sorted(list(set(
                lig.carreira.nome for lig in paragem.ligacoes
            )))
            print(f"{paragem.nome} {len(carreiras)}: {' '.join(carreiras)}")

# Exemplo de uso
if __name__ == "__main__":
    sistema = SistemaTransporte()
    
    while True:
        comando = input().strip()
        if not comando:
            continue
        
        partes = comando.split()
        cmd = partes[0]
        
        if cmd == 'q':
            break
        elif cmd == 'c':
            if len(partes) == 1:
                sistema.listar_carreiras()
            else:
                nome = ' '.join(partes[1:])
                if sistema.adicionar_carreira(nome):
                    print(f"Carreira {nome} criada")
                else:
                    print(f"Carreira {nome} já existe")
        elif cmd == 'p':
            if len(partes) == 1:
                sistema.listar_paragens()
            elif len(partes) == 2:
                nome = partes[1]
                paragem = next((p for p in sistema.paragens if p.nome == nome), None)
                if paragem:
                    print(f"{paragem.lat:.12f} {paragem.lng:.12f}")
                else:
                    print(f"{nome}: no such stop")
            elif len(partes) == 4:
                nome, lat, lng = partes[1], float(partes[2]), float(partes[3])
                if sistema.adicionar_paragem(nome, lat, lng):
                    print(f"Paragem {nome} criada")
                else:
                    print(f"{nome}: stop already exists")
        elif cmd == 'l':
            if len(partes) == 6:
                resultado = sistema.adicionar_ligacao(partes[1], partes[2], partes[3], float(partes[4]), float(partes[5]))
                if resultado != "Ligação adicionada":
                    print(resultado)
        elif cmd == 'i':
            sistema.intersecoes()
        elif cmd == 'r':
            nome = ' '.join(partes[1:])
            # Implementar remoção de carreira
        elif cmd == 'e':
            nome = ' '.join(partes[1:])
            # Implementar remoção de paragem
        elif cmd == 'a':
            # Implementar limpeza do sistema
            pass