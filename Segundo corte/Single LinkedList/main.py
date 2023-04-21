import pygame
from single_linked_list import SingleLinkedList
from colorama import Fore, init
init()
pygame.init
inst_single_linked_list= SingleLinkedList()
inst_single_linked_list.create_node_sll_ends('Spider man')
inst_single_linked_list.create_node_sll_ends('Thor')
inst_single_linked_list.create_node_sll_ends('Superman')
inst_single_linked_list.create_node_sll_unshift('Batman')
inst_single_linked_list.show_list()

print('-----------------FUNCIONES PARA ELIMINAR------------------------')
# inst_single_linked_list.delete_node_sll_pop()
# inst_single_linked_list.shift_node_sll()
inst_single_linked_list.remove_node(1)
inst_single_linked_list.show_list()

print('-----------------DEVOLVER NODO----------------------')
print(inst_single_linked_list.get_node(2).value)
inst_single_linked_list.get_node_value(3)

print('-----------------ACTUALIZAR NODO--------------------')
inst_single_linked_list.update_node_value(1, 'Flash')
inst_single_linked_list.show_list()

                