
git reset --hard
git pull
cd ../..
bench --site $1 migrate

cp apps/frappe_pos_sync/frappe_pos_sync/public/core/taxes_and_totals.py apps/erpnext/erpnext/controllers/
bench --site $1 clear-cache
bench restart