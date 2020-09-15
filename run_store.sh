echo "Run pypiplot.."
python pypiplot/pypiplot.py -u 'erdogant' -p 'D://PY/REPOSITORIES/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap.html'
read -p "Press [Enter] key to close window..."

echo ""
echo "Go to dir: erdogant.github.io"
cd D:\PY\REPOSITORIES\erdogant.github.io

echo ""
echo "Push to git"
git pull
git add .
git commit -m "update pypiplot"
git push