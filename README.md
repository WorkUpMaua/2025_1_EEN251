# 🔐 Fechadura Eletrônica Acoplável

## ➡️Descrição

Projeto desenvolvido como parte da disciplina **Microcontroladores e Sistemas Embarcados (EEN251)**, com o objetivo de criar uma **fechadura eletrônica acoplável a uma chave física**, capaz de girá-la no sentido **horário** (para trancar) e **anti-horário** (para destrancar) de forma automatizada.

## 📋 Especificação de Requisitos

| ID     | Descrição                                                                 | Tipo        |
|--------|---------------------------------------------------------------------------|-------------|
| REQ01  | O sistema deve receber comandos via entrada serial Bluetooth.             | Obrigatório |
| REQ02  | O sistema deve interpretar o caractere **"a"** como comando para abrir a fechadura. | Obrigatório |
| REQ03  | O sistema deve interpretar o caractere **"f"** como comando para fechar a fechadura. | Obrigatório |
| REQ04  | O sistema deve girar a chave no sentido **anti-horário** ao receber o comando de abrir. | Obrigatório |
| REQ05  | O sistema deve girar a chave no sentido **horário** ao receber o comando de fechar. | Obrigatório |
| REQ06  | O sistema deve ser controlado por um microcontrolador **Raspberry Pi Pico**. | Obrigatório |
| REQ07  | O código de controle deve ser implementado em **MicroPython**.            | Obrigatório |
| REQ08  | A estrutura física da fechadura deve ser produzida com impressão 3D.      | Obrigatório |
| REQ09  | O sistema pode incluir um LED indicador de status (aberto/fechado).       | Opcional    |
| REQ10  | O sistema pode incluir sensores de fim de curso para detectar o limite da rotação. | Opcional    |
| REQ11  | O sistema pode ser alimentado por fonte externa com bateria de backup.    | Opcional    |

## 🧰 Materiais Necessários

| Item | Componente                           | Descrição                                                                 | Quantidade | Valor |
|------|--------------------------------------|---------------------------------------------------------------------------|------------|------------|
| 1    | [Raspberry Pi Pico](https://www.newark.com/pt-BR/raspberry-pi/raspberry-pi-pico/raspberry-pi-board-arm-cortex/dp/22AJ1097?src=raspberrypi)                  | Controlador principal do sistema             | 1          | USD 4.00         |
| 2    | [Módulo Bluetooth HC-08](https://www.usinainfo.com.br/modulo-bluetooth-arduino/modulo-bluetooth-hc-08-40-ble-para-arduino-compativel-com-iphone-e-ipad-masterslave-3673.html)              | Comunicação serial com o celular via Bluetooth                            | 1          | BRL 61.33           |
| 3    | [Servo motor MG996](https://www.usinainfo.com.br/servo-motores/servo-motor-mg996r-tower-pro-180-11kgfcm-de-posicao-com-engrenagens-metalicas-4850.html)                    | Atuação física: gira a chave para trancar/destrancar                      | 1          |     BRL 68.77       |
| 4    | [Fonte 5V – 2A](https://www.makerhero.com/produto/fonte-dc-chaveada-5v-2a-micro-usb/)                        | Alimentação estável para o sistema                                        | 1          | BRL  29.90          |
| 5    | [Kit jumper macho x macho](https://www.makerhero.com/produto/jumpers-macho-macho-x40-unidades/)             | Conexão entre os pinos do Raspberry Pi e os módulos                       | 1          | BRL 11.90           |
| 6    | [Kit jumper macho x fêmea](https://www.makerhero.com/produto/jumpers-macho-femea-x40-unidades/)             | Alternativa de conexão entre módulos e o Raspberry Pi                     | 1          |   BRL 9.90         |
| 7    | [Mini Protoboard (Proto 170 pinos)](https://produto.mercadolivre.com.br/MLB-3405650891-mini-protoboard-breadboard-170-pontos-branco-_JM#polycard_client=search-nordic&position=14&search_layout=grid&type=item&tracking_id=51bbf8e7-26f2-46df-8383-e30ef595810f&wid=MLB3405650891&sid=search)    | Montagem de conexões temporárias durante testes                           | 1          |    BRL 13.15        |
| 8    | [Fechadura simples](https://www.leroymerlin.com.br/fechadura-soprano-para-porta-de-entrada-preto40mm-chave-simples-ipanema_91083552?referrer=category-page)    | Montagem do protótipo                           | 1          |    BRL 49.90       |
| 9    | [Kit 3 Dobradiças](https://www.mercadolivre.com.br/kit-3-dobradicas-porta-madeira-35-unio-mundial/p/MLB23541528?searchVariation=MLB23541528#polycard_client=search-nordic&searchVariation=MLB23541528&wid=MLB4008249323&position=8&search_layout=grid&type=product&tracking_id=ef2d02ef-f47d-4eea-88f2-f46553eddf61&sid=search)    | Montagem do protótipo                          | 1          |    BRL 15.17       |
| 10    | [Placa MDF 12mm 2750x1850mm](https://www.leomadeiras.com.br/p/10280500/mdf-cru-12mm-2750x1850mm-grandes-marcas#wrapper)    | Montagem do protótipo                          | 1          |    BRL 155.90       |





