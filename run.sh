docker image build -t test_api .
docker run  --network="host" test_api:latest