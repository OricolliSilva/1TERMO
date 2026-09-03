# 🌐 Arquitetura IoT (Internet das Coisas)

## 📝 1. Conteúdo Programático das Aulas
*   **Introdução à IoT**: Conceitos, histórico e ecossistema global.
*   **Arquitetura em Camadas**: Dispositivos (Edge), Redes (Gateway) e Nuvem (Cloud).
*   **Hardware para IoT**: Sensores, atuadores e microcontroladores.
*   **Protocolos de Comunicação**: MQTT, HTTP, CoAP e LoRaWAN.
*   **Sistemas Embarcados**: Desenvolvimento firmware e processamento local.
*   **Integração e Analytics**: Nuvem, bancos de dados temporais e dashboards.

---

## 🤖 2. Ecossistema Arduino
*   **Hardware Livre**: Placas acessíveis baseadas em microcontroladores (Ex: ATmega328P).
*   **IDE Arduino**: Ambiente de desenvolvimento multiplataforma simples.
*   **Ciclo de Vida**: Execução baseada em hardware dedicado sem sistema operacional.
*   **Aplicações IoT**: Placas com Wi-Fi/Bluetooth integrado (Ex: ESP32 e Arduino Nano 33 IoT).

### ⚙️ Estrutura Básica do Código (Firmware)
```cpp
// Executa uma única vez quando a placa liga ou reinicia
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Configura o pino do LED como saída
}

// Executa em loop infinito continuamente
void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Liga o LED
  delay(1000);                     // Aguarda 1 segundo
  digitalWrite(LED_BUILTIN, LOW);  // Desliga o LED
  delay(1000);                     // Aguarda 1 segundo
}
```

---

## 💻 3. Programação C++ para IoT
*   **Performance**: Linguagem compilada com controle direto de memória e hardware.
*   **Eficiência**: Ideal para dispositivos com recursos severamente limitados (RAM/Flash).
*   **Tipagem Estática**: Erros de tipo são validados durante a compilação.
*   **Uso em IoT**: Desenvolvimento de firmware nativo para microcontroladores.

### 🔬 Exemplo: Leitura de Sensor Analógico
```cpp
const int SENSOR_PIN = A0; 
int valorSensor = 0;

void setup() {
  Serial.begin(115200); // Inicializa comunicação serial
}

void loop() {
  valorSensor = analogRead(SENSOR_PIN); // Lê o pino analógico
  Serial.print("Leitura do Sensor: ");
  Serial.println(valorSensor);
  delay(500);
}
```

---

## 🐍 4. Programação Python para IoT
*   **Alto Nível**: Linguagem interpretada, focada em produtividade e legibilidade.
*   **Ecossistema**: Bibliotecas ricas para IA, ciência de dados e protocolos de rede.
*   **Uso em IoT**: Gateways (Ex: Raspberry Pi), processamento de dados e scripts na nuvem.
*   **MicroPython**: Versão otimizada do Python para rodar diretamente em microcontroladores.

### 🛰️ Exemplo: Cliente MQTT para Envio de Dados (Paho-MQTT)
```python
import time
import random
import paho.mqtt.client as mqtt

# Configurações do Broker
BROKER = "hivemq.com"
TOPICO = "iot/aula/temperatura"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    temp_simulada = round(random.uniform(20.0, 30.0), 2)
    # Envia o dado para o broker MQTT
    client.publish(TOPICO, payload=str(temp_simulada))
    print(f"Dados enviados: {temp_simulada}°C")
    time.sleep(2)
```
