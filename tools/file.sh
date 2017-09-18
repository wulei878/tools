result=`find /Users/owen/workspace/Memory/Memory/Assets.xcassets -name "*.jpeg"`
for var in $result
do
	cp $var "/Users/owen/Documents/Memory/images/"
done