# one line to give the program's name and a brief description.
# Copyright © 2022 yourname

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from class_impuesto import Carro


def main():

    while True:
        try:
            iplaca = input("Ingrese la placa:  ")
            itipo = int(input("Ingrese el tipo: "))
            imodelo = int(input("Ingrese el modelo: "))

            parametros = {"placa": iplaca, "tipo": itipo, "modelo": imodelo}

            carro = Carro(**parametros)
            impuesto = carro.get_impuesto()

            print(f"El impuesto es el {impuesto}% del valor comercial\n")

            seguir = input("Desea segur ingresando datos?? S o N: ")[0]
            if seguir == "n" or seguir == "N":
                break
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
