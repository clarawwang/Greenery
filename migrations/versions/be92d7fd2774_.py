"""empty message

Revision ID: be92d7fd2774
Revises: 5ff975e68e60
Create Date: 2020-09-20 05:48:22.125380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be92d7fd2774'
down_revision = '5ff975e68e60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_info', schema=None) as batch_op:
        batch_op.drop_column('bf2')
        batch_op.drop_column('lf2')
        batch_op.drop_column('distance')
        batch_op.drop_column('enSource')
        batch_op.drop_column('df2')
        batch_op.drop_column('df3')
        batch_op.drop_column('lf1')
        batch_op.drop_column('enAmt')
        batch_op.drop_column('transport')
        batch_op.drop_column('bf1')
        batch_op.drop_column('df1')
        batch_op.drop_column('bf3')
        batch_op.drop_column('lf3')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lf3', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('bf3', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('df1', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('bf1', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('transport', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('enAmt', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('lf1', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('df3', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('df2', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('enSource', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('distance', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('lf2', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('bf2', sa.VARCHAR(length=100), nullable=True))

    # ### end Alembic commands ###
