# One line to give the program's name and a brief description.
# Copyright © 2022 yourname

# This program  is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

class Carro(object):

    """Docstring for Carro. """

    def __init__(self, **kwargs):
        self.placa = kwargs["placa"]
        self.tipo = kwargs["tipo"]
        self.modelo = kwargs["modelo"]

    def __set_tipo(self, valor: int):
        if isinstance(valor, int):
            if valor > 3 or valor < 1:
                raise ValueError("Solo se permite 1, 2 o 3")
        self._tipo = (0, 1)[valor == 3]

    def __set_model(self, valor):
        if isinstance(valor, int):
            if valor < 2001 or valor > 2022:
                raise ValueError("El año debe ser mayor a 2000 y menor a 2023")
        self._modelo = (2, 1)[valor >= 2010]

    def __set_placa(self, valor):
        if len(valor) > 6:
            raise ValueError("La placa no puede tener mas de 6 caracteres")
        self._placa = valor

    def get_impuesto(self) -> int:
        impuesto: int

        tabla = {1: [10, 15], 2: [20, 55]}

        impuesto = tabla[self._modelo][self._tipo]
        return impuesto

    placa = property(fset=__set_placa)
    tipo = property(fset=__set_tipo)
    modelo = property(fset=__set_model)
