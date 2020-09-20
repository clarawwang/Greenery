"""empty message

Revision ID: 22593bbefc63
Revises: 8fe085afc5f6
Create Date: 2020-09-20 04:07:36.197579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22593bbefc63'
down_revision = '8fe085afc5f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_info', sa.Column('week', sa.Integer(), nullable=True))
    op.drop_column('user_info', 'lf3')
    op.drop_column('user_info', 'lf2')
    op.drop_column('user_info', 'df3')
    op.drop_column('user_info', 'transport')
    op.drop_column('user_info', 'distance')
    op.drop_column('user_info', 'bf3')
    op.drop_column('user_info', 'bf1')
    op.drop_column('user_info', 'lf1')
    op.drop_column('user_info', 'bf2')
    op.drop_column('user_info', 'enSource')
    op.drop_column('user_info', 'df1')
    op.drop_column('user_info', 'enAmt')
    op.drop_column('user_info', 'df2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_info', sa.Column('df2', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('enAmt', sa.INTEGER(), nullable=True))
    op.add_column('user_info', sa.Column('df1', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('enSource', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('bf2', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('lf1', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('bf1', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('bf3', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('distance', sa.INTEGER(), nullable=True))
    op.add_column('user_info', sa.Column('transport', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('df3', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('lf2', sa.VARCHAR(length=100), nullable=True))
    op.add_column('user_info', sa.Column('lf3', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('user_info', 'week')
    # ### end Alembic commands ###
