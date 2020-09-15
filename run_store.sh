echo "Run pypiplot.."
python pypiplot/pypiplot.py -u 'erdogant' -p 'D://PY/REPOSITORIES/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap.html'

echo ""
read -p "Press [Enter] to push to Git.."

echo ""
echo "Go to dir: erdogant.github.io"
cd D://PY/REPOSITORIES/erdogant.github.io

echo ""
git pull
git add .
git commit -m "update pypiplot"
git push

echo ""
read -p "Press [Enter] to close"
