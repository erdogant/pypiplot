cd D://REPOS/pypiplot

echo "Run pypiplot.."
python pypiplot/pypiplot.py -u 'erdogant' -p 'D://REPOS/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap.html' -v '700'

echo ""
read -p "Press [Enter] to push to Git.."

echo ""
echo "Go to dir: erdogant.github.io"
cd D://REPOS/erdogant.github.io

echo ""
git pull
git add .
git commit -m "update pypiplot"
git push

echo ""
read -p "Press [Enter] to close"
