package helpers

import (
	"context"
	"fmt"
	"log"
	"os"
	"strings"
	"time"

	"github.com/segmentio/kafka-go"
)

func CreateKafkaWriter(topic string, writerConfig kafka.WriterConfig) (*kafka.Writer, error) {
	writer := kafka.NewWriter(writerConfig)
	return writer, nil
}

func SendMessage(writer *kafka.Writer, message string) error {
	var messages []kafka.Message
	messages = append(messages, kafka.Message{
		Value: []byte(message),
	})

	return writer.WriteMessages(context.Background(), messages...)
}

func GetEnvOrPanic(key string) string {
	value := os.Getenv(key)
	if value == "" {
		log.Fatal(fmt.Sprintf("Environment variable %s not set", key))
	}
	return value
}

func GetEnvironmentVariable(key string) (string, bool) {
	value := os.Getenv(key)
	return value, value!= ""
}

func GetKafkaConfig() kafka.WriterConfig {
	brokers := GetEnvOrPanic("KAFKA_BROKERS")
	topic := GetEnvOrPanic("KAFKA_TOPIC")
	kafkaConfig := kafka.WriterConfig{
		Topic:               topic,
		Brokers:             strings.Split(brokers, ","),
		Balancer:            kafka.LeastConnectionsBalancer{},
		RequiredAcks:        kafka.RequireAll,
		MaxRandomWait:       100 * time.Millisecond,
		MaxWait:             500 * time.Millisecond,
		Retry:               kafka.NewSimpleRetry(10),
	}
	return kafkaConfig
}