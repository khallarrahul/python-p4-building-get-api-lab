"""updates tables

Revision ID: e3bd682a8200
Revises: 36699a998047
Create Date: 2023-09-04 14:17:10.050453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3bd682a8200'
down_revision = '36699a998047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.drop_constraint('uq_baked_goods_name', type_='unique')

    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.drop_constraint('uq_bakeries_name', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_bakeries_name', ['name'])

    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_baked_goods_name', ['name'])

    # ### end Alembic commands ###
