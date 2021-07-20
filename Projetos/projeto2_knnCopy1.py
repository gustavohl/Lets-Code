#!/usr/bin/env python
# coding: utf-8

# In[85]:ab


class Knn_classificacao:
    def __init__(self, dados_class, dados_noclass,ind_id, ind_class, ind_coord):    
        ''' dados_class: dados de referência já classificados.
            dados_noclass: dados a serem classificados.
            ind_id: elemento identificador da amostra.
            ind_class: índice em que a classificação do elemento na lista de referência está localizado.
            ind_coord: índice em que os valores responsável pela classificação do elemento das listas estão localizados.
        '''
        self.dados_class = dados_class
        self.dados_noclass = dados_noclass
        self.ind_id = ind_id
        self.ind_class = ind_class
        self.ind_coord = ind_coord
        
    def dist_eucl(self, noclass_elem):
        ''' noclasse_elem: elemento não classificado.
            class_elem: elemento da lista de referência com dados classificados.
            dist: distância euclidiana entre valores da lista de referência e lista não classificada.
            distancias_classificadas: lista com as distâncias entre um elemento não classificado e todos os elementos de referência com suas respectivas classificações.
        '''
        distancias_classificadas = []
        for class_elem in self.dados_class:
            dist = (sum([(x - y) ** 2 for x, y in zip(noclass_elem[self.ind_coord], class_elem[self.ind_coord])])) ** (0.5)
            distancias_classificadas.append([dist, class_elem[self.ind_class]])
        return distancias_classificadas
            
    def classificar_um(self, noclass_elem, k):
        ''' distancias_organizadas: distâncias euclidianas organizas do menor para o maior
            profiles: lista com todas as classificações contidas na lista de referência
            contador: variável para verificar qual a classificação com maior ocorrência
            classificacao: saída com a classificacão que teve maior ocorrência
        '''
        distancias_organizadas = self.dist_eucl(noclass_elem)
        distancias_organizadas.sort()
        profiles = list(set(user_class[self.ind_class] for user_class in self.dados_class))
        contador = 0
        classificacao = ''
        for profile in profiles:
            if contador < (list(zip(*distancias_organizadas[:k]))[1]).count(profile):
                contador = (list(zip(*distancias_organizadas[:k]))[1]).count(profile)
                classificacao = profile
        return classificacao
    
    def classificar_todos(self, k):
        classificados = {}
        for noclass_elem in self.dados_class:
            classificados[noclass_elem[self.ind_id]] = self.classificar_um(noclass_elem, k)
            
        return classificados

