#!/bin/bash
set  -e

REQUIRED_CMDS=("kubectl" "docker" "minikube")

echo "Checking the environment... "

# checking the above tools are installed or not
for cmd in "${REQUIRED_CMDS[@]}"; do   # @ will help to read each item from the above array
    if ! command -v $cmd &>/dev/null;then   #  command -v  is a command which return the path of the exe of a tool.  Here its just verifying it only- yes or 							no . So returning STDMSG and STDERR has to be moved to the /dev/null file, so that user cant see it.
	echo "X  $cmd not found. Install it. "
	exit 1
    fi
done 

CURRENT_CONTEXT=$(kubectl config current-context)
# checking the context of the Kubernete. Make sure its in minikube

if [[ "$CURRENT_CONTEXT" != "minikube" ]];  then
   echo "Kubectl context is  '$CURRENT_CONTEXT' "
   echo "Switch to minikube:  kubectl config use-context minikube"
   exit 1
fi



echo "Environment looks good"

