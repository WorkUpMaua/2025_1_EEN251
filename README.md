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
| REQ08  | A estrutura física da fechadura deve ser produzida com corte a laser em MDF.      | Obrigatório |
| REQ09  | O sistema deve ser alimentado por pilhas    | Obrigatório    |
| REQ10  | O sistema pode incluir um LED indicador de status (aberto/fechado).       | Opcional    |


## 🧰 Materiais Necessários

| Item | Componente                           | Descrição                                                                 | Quantidade | Valor |
|------|--------------------------------------|---------------------------------------------------------------------------|------------|------------|
| 1    | [Raspberry Pi Pico](https://www.newark.com/pt-BR/raspberry-pi/raspberry-pi-pico/raspberry-pi-board-arm-cortex/dp/22AJ1097?src=raspberrypi)                  | Controlador principal do sistema             | 1          | USD 4.00         |
| 2    | [Módulo Bluetooth HC-08](https://www.usinainfo.com.br/modulo-bluetooth-arduino/modulo-bluetooth-hc-08-40-ble-para-arduino-compativel-com-iphone-e-ipad-masterslave-3673.html)              | Comunicação serial com o celular via Bluetooth                            | 1          | BRL 61.33           |
| 3    | [Servo motor SG-5010](https://www.usinainfo.com.br/servo-motores/servo-motor-mg996r-tower-pro-180-11kgfcm-de-posicao-com-engrenagens-metalicas-4850.html](https://protosupplies.com/product/servo-motor-sg-5010/))                    | Atuação física: gira a chave para trancar/destrancar                      | 1          |     USD 6.95       |
| 4    | [Pilha de lítio recarregável (2 unidades) ](https://produto.mercadolivre.com.br/MLB-3425451069-bateria-18650-2600mah-37v-bap-energy-kit-02pcs--_JM#polycard_client=search-nordic&position=9&search_layout=grid&type=item&tracking_id=4fb48910-bb5a-4e5d-b31b-5b39cf1b8640&wid=MLB3425451069&sid=search)                        | Alimentação estável para o sistema                                        | 1          | BRL  87.82          |
| 5    | [Kit jumper macho x macho](https://www.makerhero.com/produto/jumpers-macho-macho-x40-unidades/)             | Conexão entre os pinos do Raspberry Pi e os módulos                       | 1          | BRL 11.90           |
| 6    | [Kit jumper macho x fêmea](https://www.makerhero.com/produto/jumpers-macho-femea-x40-unidades/)             | Alternativa de conexão entre módulos e o Raspberry Pi                     | 1          |   BRL 9.90         |
| 7    | [Mini Protoboard (Proto 170 pinos)](https://produto.mercadolivre.com.br/MLB-3405650891-mini-protoboard-breadboard-170-pontos-branco-_JM#polycard_client=search-nordic&position=14&search_layout=grid&type=item&tracking_id=51bbf8e7-26f2-46df-8383-e30ef595810f&wid=MLB3405650891&sid=search)    | Montagem de conexões temporárias durante testes                           | 1          |    BRL 13.15        |
| 8    | [Fechadura simples](https://www.leroymerlin.com.br/fechadura-soprano-para-porta-de-entrada-preto40mm-chave-simples-ipanema_91083552?referrer=category-page)    | Montagem do protótipo                           | 1          |    BRL 49.90       |
| 9    | [Placa MDF 12mm 2750x1850mm](https://www.leomadeiras.com.br/p/10280500/mdf-cru-12mm-2750x1850mm-grandes-marcas#wrapper)    | Montagem do protótipo                          | 1          |    BRL 155.90       |
| 10    | [Conversor de Nível Lógico](https://www.leomadeiras.com.br/p/10280500/mdf-cru-12mm-2750x1850mm-grandes-marcas#wrapper](https://www.eletrogate.com/conversor-de-nivel-logico-33-5v-bidirecional))    | Adapta sinais digitais entre diferentes níveis de tensão                         | 1          |    BRL 4.90       |
| 11    | [Módulo Regulador de Tensão](https://www.eletrogate.com/modulo-regulador-de-tensao-step-down-lm2596)    |   Converte a tensão de entrada para um nível adequado de alimentação                      | 1          |    BRL 10.90       |
| 12    | [Switch](https://www.eletrogate.com/modulo-regulador-de-tensao-step-down-lm2596](https://www.mercadolivre.com.br/micro-chave-17101-alavanca-unipolar-ligaliga-1a-2-posicoes/p/MLB40891000?searchVariation=MLB40891000#polycard_client=search-nordic&searchVariation=MLB40891000&wid=MLB3888971897&position=7&search_layout=grid&type=product&tracking_id=392b5b42-78c2-4b5d-98c5-98e57b20f13e&sid=search))    |   Controla o acionamento do sistema, permitindo ligar ou desligar                       | 1          |    BRL 37.80       |

## 🔧 Diagrama de Blocos do Projeto

O diagrama de blocos a seguir tem como objetivo representar, de forma simplificada, a estrutura funcional do projeto eletrônico. Ele ilustra como os principais componentes — como fontes de energia, microcontrolador, atuadores e módulos de comunicação — estão interconectados e como o fluxo de energia e sinais percorre o sistema. Essa visão geral facilita o entendimento da lógica de funcionamento do circuito e orienta tanto o desenvolvimento quanto a montagem prática do projeto.

![Imagem do Diagrama de Blocos](docs/diagrama_de_blocos.svg)



