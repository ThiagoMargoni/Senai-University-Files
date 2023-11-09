#include <PubSubClient.h>
#include <WiFi.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
const char* ssid = "Redmi Note 10 5G";
const char* password = "raphael2";
const char* mqtt_server = "test.mosquitto.org";

#define DHTPIN 4
#define DHTTYPE DHT22
#define MSG_BUFFER_SIZE (50)

char msg[MSG_BUFFER_SIZE];
DHT_Unified dht(DHTPIN, DHTTYPE);

uint32_t delayMS;
unsigned long lastMsg = 0;
int value = 0;
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.println(F("Sensor DHT22"));
  sensor_t sensor;

  setup_WiFi();
  client.setServer(mqtt_server, 1883);

  dht.temperature().getSensor(&sensor);
  Serial.println(F("---------------------------------"));
  Serial.println(F("Temperatura"));
  Serial.println(F("Sensor: "));
  Serial.print(sensor.name);
  Serial.println(F("Valor máximo: "));
  Serial.print(sensor.max_value);
  Serial.println(F("°C"));
  Serial.print(F("Valor mínimo: "));
  Serial.print(sensor.min_value);
  Serial.println(F("°C"));
  Serial.print(F("Resolução: "));
  Serial.print(sensor.resolution);
  Serial.println(F("°C"));
  Serial.println(F("---------------------------------"));

  dht.humidity().getSensor(&sensor);
  Serial.println(F("---------------------------------"));
  Serial.println(F("Umidade"));
  Serial.println(F("Sensor: "));
  Serial.println(sensor.name);
  Serial.print(F("Valor máximo: "));
  Serial.print(sensor.max_value);
  Serial.println(F("%"));
  Serial.print(F("Valor mínimo: "));
  Serial.print(sensor.min_value);
  Serial.println(F("%"));
  Serial.print(F("Resolução: "));
  Serial.print(sensor.resolution);
  Serial.println(F("%"));
  Serial.println(F("---------------------------------"));
  delayMS = sensor.min_delay / 1000;
}

void setup_WiFi() {
  delay(10);
  Serial.println("");
  Serial.print("conectando com");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi conectando");
  Serial.println("IP: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Aguardando conexão MQTT...");
    String clientId = "ESP32Client";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      Serial.println("conectado");

      sensors_event_t event;  // Declare event here
    } else {
      Serial.print("falhou, rc=");
      Serial.print(client.state());
      Serial.print("tente novamente em 5s");
      delay(500);
    }
  }
}

void loop() {
  delay(delayMS);
  sensors_event_t event;

  dht.temperature().getEvent(&event);
  if (isnan(event.temperature)) {
    Serial.println(F("ERRO NA LEITURA DA TEMPERATURA"));
  } else {
    Serial.print(F("temperatura:"));
    Serial.print(event.temperature);
    Serial.println(F("°C"));
    sprintf(msg, "%f", event.temperature);
    client.publish("raphael_thiago/temperatura", msg);

    if(event.temperature > 22) {
      sprintf(msg, "%i", 1);
      client.publish("raphael_thiago/ventilador", msg); // ligado
    } else {
      sprintf(msg, "%i", 0);
      client.publish("raphael_thiago/ventilador", msg); // desligado
    }
  }

  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) {
    Serial.println(F("ERRO NA LEITURA DA TEMPERATURA"));
  } else {
    Serial.print(F("umidade:"));
    Serial.print(event.relative_humidity);
    Serial.println(F("%"));
    sprintf(msg, "%f", event.relative_humidity);
    client.publish("raphael_thiago/umidade", msg);

    if(event.relative_humidity <= 60) {
      sprintf(msg, "%i", 1);
      client.publish("raphael_thiago/umidificador", msg); // ligado
    } else {
      sprintf(msg, "%i", 0);
      client.publish("raphael_thiago/umidificador", msg); // desligado
    }
  }

  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
