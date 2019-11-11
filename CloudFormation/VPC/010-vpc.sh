#!/bin/sh

CFN_TEMPLATE="vpc-test.yaml"
CFN_STACKNAME="vpc-test-stack"

CHANGESET_OPTION="--no-execute-changeset"

if [ $# = 1 ] && [ $1 = "check" ]; then
    echo "validate-template mode"
    # テンプレートチェックの実行
    aws cloudformation validate-template --template-body file://${CFN_TEMPLATE}
    exit 0
fi

if [ $# = 1 ] && [ $1 = "del" ]; then
    echo "delete mode"
    # テンプレート削除を実行
    aws cloudformation delete-stack --stack-name ${CFN_STACKNAME}
    exit 0
fi

if [ $# = 1 ] && [ $1 = "deploy" ]; then
    echo "deploy mode"
    CHANGESET_OPTION=""
fi

# テンプレートの実行
aws cloudformation deploy --stack-name ${CFN_STACKNAME} --template-file ${CFN_TEMPLATE} ${CHANGESET_OPTION}
#  --parameter-overrides \
#  NameTagPrefix=prd \
#  VPCCIDR=10.70

exit 0