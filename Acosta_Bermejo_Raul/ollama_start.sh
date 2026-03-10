#
#
#
#DIR_IP=100.113.158.78
export DIR_IP="0.0.0.0"
export PORT="11434"
#export OLLAMA_API_BASE="http://$DIR_IP:$PORT"
export OLLAMA_HOST="http://$DIR_IP:$PORT"
ollama serve &

ps -fea | grep -i ollama
lsof -i :$PORT
netstat -an | grep $PORT

curl http://$DIR_IP:$PORT

