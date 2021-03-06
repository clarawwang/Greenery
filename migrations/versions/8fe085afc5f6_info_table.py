"""info table

Revision ID: 8fe085afc5f6
Revises: f2c385768eb3
Create Date: 2020-09-20 02:03:38.814807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fe085afc5f6'
down_revision = 'f2c385768eb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_info', sa.Column('apple', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('avocado', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('banana', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('bean', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('beef', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('beer', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('berry', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('bread', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('bus', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('cheese', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('chicken', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('citrus', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('coffee', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('ecar', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('egg', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('electricity', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('enOut', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('fish', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('foodOut', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('fuel', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('gas', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('gcar', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('lamb', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('milk', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('nut', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('oat', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('pasta', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('pea', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('pl_milk', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('plane', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('pork', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('potato', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('prawn', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('propane', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('rice', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('tea', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('tofu', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('tomato', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('train', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('transOut', sa.Integer(), nullable=True))
    op.add_column('user_info', sa.Column('wine', sa.Integer(), nullable=True))
    op.drop_column('user_info', 'bf3')
    op.drop_column('user_info', 'transport')
    op.drop_column('user_info', 'df1')
    op.drop_column('user_info', 'df2')
    op.drop_column('user_info', 'df3')
    op.drop_column('user_info', 'enSource')
    op.drop_column('user_info', 'lf3')
    op.drop_column('user_info', 'lf2')
    op.drop_column('user_info', 'enAmt')
    op.drop_column('user_info', 'lf1')
    op.drop_column('user_info', 'bf2')
    op.drop_column('user_info', 'distance')
    op.drop_column('user_info', 'bf1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_info', sa.Column('bf1', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('distance', sa.INTEGER(), nullable=True))
    op.add_column('user_info', sa.Column('bf2', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('lf1', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('enAmt', sa.INTEGER(), nullable=True))
    op.add_column('user_info', sa.Column('lf2', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('lf3', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('enSource', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('df3', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('df2', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('df1', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('transport', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('bf3', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('user_info', 'wine')
    op.drop_column('user_info', 'transOut')
    op.drop_column('user_info', 'train')
    op.drop_column('user_info', 'tomato')
    op.drop_column('user_info', 'tofu')
    op.drop_column('user_info', 'tea')
    op.drop_column('user_info', 'rice')
    op.drop_column('user_info', 'propane')
    op.drop_column('user_info', 'prawn')
    op.drop_column('user_info', 'potato')
    op.drop_column('user_info', 'pork')
    op.drop_column('user_info', 'plane')
    op.drop_column('user_info', 'pl_milk')
    op.drop_column('user_info', 'pea')
    op.drop_column('user_info', 'pasta')
    op.drop_column('user_info', 'oat')
    op.drop_column('user_info', 'nut')
    op.drop_column('user_info', 'milk')
    op.drop_column('user_info', 'lamb')
    op.drop_column('user_info', 'gcar')
    op.drop_column('user_info', 'gas')
    op.drop_column('user_info', 'fuel')
    op.drop_column('user_info', 'foodOut')
    op.drop_column('user_info', 'fish')
    op.drop_column('user_info', 'enOut')
    op.drop_column('user_info', 'electricity')
    op.drop_column('user_info', 'egg')
    op.drop_column('user_info', 'ecar')
    op.drop_column('user_info', 'coffee')
    op.drop_column('user_info', 'citrus')
    op.drop_column('user_info', 'chicken')
    op.drop_column('user_info', 'cheese')
    op.drop_column('user_info', 'bus')
    op.drop_column('user_info', 'bread')
    op.drop_column('user_info', 'berry')
    op.drop_column('user_info', 'beer')
    op.drop_column('user_info', 'beef')
    op.drop_column('user_info', 'bean')
    op.drop_column('user_info', 'banana')
    op.drop_column('user_info', 'avocado')
    op.drop_column('user_info', 'apple')
    # ### end Alembic commands ###
