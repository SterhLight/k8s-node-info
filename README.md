# K8S NODE INFO

# k8s-node-info

Простое веб-приложение на Flask, предназначенное для отображения имени Pod и Node внутри кластера Kubernetes. Предоставляется Helm-чарт для развёртывания как `DaemonSet`.

## Что делает приложение

Приложение запускается на порту `80` и возвращает HTML-страницу с информацией:

- Pod name (определяется через `socket.gethostname()`)
- Node name (читается из переменной окружения `NODE_NAME`)

Пример вывода:

```html
<h1>Hello from Kubernetes!</h1>
<p>Pod name: k8s-node-info-abc123</p>
<p>Node name: worker-node-1</p>

## Сборка Docker-образа

```bash
docker build -t your-registry/k8s-node-info:latest ./app
```

## Установка через Helm

```bash
helm upgrade --install k8s-node-info ./chart/k8s-node-info --namespace monitoring --create-namespace
```

По умолчанию используется DaemonSet, чтобы запустить по одному Pod'у на каждом Node.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](./LICENSE) file for details.

## Автор

krasava
al.popytaev@yandex.ru
