if [[ $# -ne 1 ]]; then
	echo "Usage: leap.sh <year>";
	exit 1;
else
	re='^[0-9]+$';
	if ! [[ "$1" =~ $re ]]; then
		echo "Usage: leap.sh <year>";
		exit 1;
	else
		if [[ $(( $1 % 4 )) == 0 && $(( $1 % 100 )) != 0 || $(( $1 % 400 )) == 0 ]]; then
			echo "This is a leap year.";
		else
			echo "This is not a leap year.";
		fi
	fi
fi